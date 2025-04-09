from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class CallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the callback URL (e.g., `/callback?code=XXX&state=YYY`)
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        # Extract the authorization code and state
        code = query_params.get("code", [None])[0]
        state = query_params.get("state", [None])[0]
        error = query_params.get("error", [None])[0]

        if error:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f"<h1>OAuth Error: {error}</h1>".encode())
        elif code:
            # Success! Exchange the code for a token (next step).
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
                <h1>OAuth Callback Received!</h1>
                <p>Check your terminal for the authorization code.</p>
            """)
            print(f"\nAuthorization Code: {code}\nState: {state}\n")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing 'code' parameter.")

if __name__ == "__main__":
    server_address = ("localhost", 8080)
    httpd = HTTPServer(server_address, CallbackHandler)
    print("Local callback server running on http://localhost:8080")
    print("Press Ctrl+C to stop...")
    httpd.serve_forever()