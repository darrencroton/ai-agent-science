"""Unit tests for ads.py, limited to failures that are silent: two security properties,
and two ways a valid paper would look absent with nothing to say so.

A leaked token raises no error, so nothing else would catch it:

  * the token never appears in a message built from something the far end sent
    back (error body, reason phrase, redirect Location);
  * a redirect is refused, and the Authorization header never reaches its target.

A paper is likewise lost without a sound when `resolve` is handed a URL and
sends ADS a query that matches nothing, or when `export` calls a truncated
bibcode present and exits 0.

The security tests drive `_request`, which is where those messages are built;
`main` only prefixes and prints the same text, and going through it would add
argparse and stdout/stderr capture without adding coverage. The export test
does go through `main`, because the exit code is what it checks. The far end
is a stub HTTP server on 127.0.0.1, which the tool permits over plain http and
reaches without a proxy.

Run from the repository root:

    python3 -m unittest discover -s tools -p 'test_*.py'
"""

import contextlib
import http.server
import io
import json
import os
import sys
import threading
import unittest
import urllib.parse
from unittest import mock

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ads

TOKEN = "tok_Zq81xV4mR7"


class Stub(http.server.HTTPServer):
    """Answers every GET and POST with one fixed response, recording each request's
    Authorization header and path (query string included)."""

    def __init__(self, status, reason=None, headers=None, body=b""):
        super().__init__(("127.0.0.1", 0), _Handler)
        self.response = (status, reason, headers or {}, body)
        self.seen = []
        self.paths = []
        self.base = f"http://127.0.0.1:{self.server_port}"


class _Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.server.seen.append(self.headers.get("Authorization"))
        self.server.paths.append(self.path)
        self.rfile.read(int(self.headers.get("Content-Length", 0)))  # a POST body
        status, reason, headers, body = self.server.response
        self.send_response(status, reason)
        for name, value in headers.items():
            self.send_header(name, value)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    do_POST = do_GET

    def log_message(self, *args):
        pass


class Silent(unittest.TestCase):
    def setUp(self):
        # Setting the cached token skips `_find_token`, so neither the macOS
        # Keychain nor ~/.ads/dev_key is consulted and the test is hermetic.
        patches = [mock.patch.object(ads, "_TOKEN", TOKEN), mock.patch.dict(os.environ)]
        for patch in patches:
            patch.start()
            self.addCleanup(patch.stop)

    def serve(self, *args, **kwargs):
        stub = Stub(*args, **kwargs)
        thread = threading.Thread(target=stub.serve_forever, args=(0.01,), daemon=True)
        thread.start()

        def stop():
            stub.shutdown()
            stub.server_close()
            thread.join()

        self.addCleanup(stop)
        return stub

    def failure(self, stub):
        """The text of the AdsError raised by one request to `stub`."""
        os.environ["SCI_PAPER_ADS_BASE"] = stub.base + "/v1"
        with self.assertRaises(ads.AdsError) as caught:
            ads._request("search/query")
        return str(caught.exception)

    def test_error_body_is_scrubbed(self):
        stub = self.serve(
            401, body=f"debug page: Authorization: Bearer {TOKEN}".encode()
        )
        message = self.failure(stub)
        self.assertIn("HTTP 401", message)  # the error path ran, not some other one
        self.assertNotIn(TOKEN, message)

    def test_scrub_precedes_truncation(self):
        # The body is cut to 400 characters, so scrubbing afterwards would
        # leave the front of a token that straddles the cut.
        stub = self.serve(500, body=b"x" * 390 + TOKEN.encode())
        message = self.failure(stub)
        self.assertIn("HTTP 500", message)
        self.assertNotIn(TOKEN[:6], message)

    def test_reason_phrase_is_scrubbed(self):
        message = self.failure(self.serve(500, reason=f"Failed for {TOKEN}"))
        self.assertIn("HTTP 500", message)
        self.assertNotIn(TOKEN, message)

    def test_redirect_is_refused_and_scrubbed(self):
        # The Location is far-end text too: the token is echoed in both the
        # path and the query, and neither may reach the refusal message. The
        # target is on loopback so that no test can leave it if refusal regresses.
        target = self.serve(200, body=json.dumps({}).encode())
        location = f"{target.base}/{TOKEN}?key={TOKEN}"
        origin = self.serve(302, headers={"Location": location})
        message = self.failure(origin)
        self.assertIn("refused", message)
        self.assertNotIn(TOKEN, message)
        self.assertEqual(origin.seen, [f"Bearer {TOKEN}"])  # the request did go out
        self.assertEqual(target.seen, [])  # and nothing followed it

    def test_resolve_strips_url_down_to_the_identifier(self):
        # An unstripped URL builds a query that matches nothing, which reads as
        # "ADS does not have this paper". So check the query ADS is sent, not
        # only what `_resolve` says it sent.
        doc = {"bibcode": "2020ApJ...900....1A", "property": ["REFEREED"]}
        stub = self.serve(200, body=json.dumps({"response": {"docs": [doc]}}).encode())
        os.environ["SCI_PAPER_ADS_BASE"] = stub.base + "/v1"
        doi, arxiv = 'doi:"10.1088/0004-637X/900/1/1"', 'identifier:"arXiv:2001.01234"'
        for given, query in [
            ("https://doi.org/10.1088/0004-637X/900/1/1", doi),
            ("https://doi.org/10.1088/0004-637X/900/1/1?ref=x#top", doi),
            ("https://arxiv.org/abs/2001.01234v2?context=astro-ph#top", arxiv),
            ("https://arxiv.org/pdf/2001.01234v1.pdf", arxiv),
            ("https://arxiv.org/pdf/2001.01234.pdf?download=1", arxiv),
        ]:
            with self.subTest(given=given):
                ads._resolve(given, 20)
                sent = urllib.parse.parse_qs(
                    urllib.parse.urlsplit(stub.paths[-1]).query
                )
                self.assertEqual(sent["q"], [query])

    def test_export_reports_a_prefix_bibcode_missing_and_exits_3(self):
        # ADS returned `...1AB` only. A bare substring test would find `...1A`
        # inside it and call the requested bibcode present.
        bibtex = "@ARTICLE{2020ApJ...900....1AB,\n  title = {A Paper},\n}\n"
        stub = self.serve(200, body=json.dumps({"export": bibtex}).encode())
        os.environ["SCI_PAPER_ADS_BASE"] = stub.base + "/v1"
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            status = ads.main(["export", "2020ApJ...900....1A", "2020ApJ...900....1AB"])
        self.assertEqual(status, 3)
        self.assertEqual(out.getvalue(), bibtex)  # what did come back, verbatim
        self.assertEqual(
            err.getvalue(), "no BibTeX returned for: 2020ApJ...900....1A\n"
        )
        self.assertEqual(stub.paths, ["/v1/export/bibtex"])


if __name__ == "__main__":
    unittest.main()
