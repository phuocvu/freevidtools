#!/usr/bin/env python3
"""
FreeVidTools Dev Server
Run: python3 server.py
Open: http://localhost:3000
"""
import http.server
import sys

PORT = 3000

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # COOP + COEP: enables SharedArrayBuffer for FFmpeg Worker
        # "credentialless" allows cross-origin CDN resources (esm.sh, jsdelivr)
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'credentialless')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'public, max-age=86400')
        super().end_headers()

    def log_message(self, format, *args):
        msg = format % args
        if '200' in msg or '304' in msg:
            return
        sys.stderr.write(f"  {msg}\n")

if __name__ == '__main__':
    print(f"""
  ====================================
    FreeVidTools Dev Server
    http://localhost:{PORT}
  ====================================
""")
    with http.server.HTTPServer(('', PORT), CORSHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
