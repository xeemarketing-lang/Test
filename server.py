#!/usr/bin/env python3
"""Simple local server with SPA-style fallback for dashboard previews."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PORT = 8000
ROOT = Path(__file__).resolve().parent
INDEX = ROOT / "index.html"


class DashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Some preview environments request non-root paths (e.g., /preview).
        # Serve the dashboard for unknown routes instead of returning 404.
        if self.path in {"/", "", "/index.html"}:
            return super().do_GET()

        requested = (ROOT / self.path.lstrip("/")).resolve()
        if requested.exists() and str(requested).startswith(str(ROOT)):
            return super().do_GET()

        self.path = "/index.html"
        return super().do_GET()


if __name__ == "__main__":
    if not INDEX.exists():
        raise SystemExit("index.html not found in repository root.")

    server = ThreadingHTTPServer(("0.0.0.0", PORT), DashboardHandler)
    print(f"Serving dashboard on http://0.0.0.0:{PORT}")
    server.serve_forever()
