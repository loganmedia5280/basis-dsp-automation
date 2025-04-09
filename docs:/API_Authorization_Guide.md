# Basis API OAuth 2.0 Flow (Dev)
*How this system authenticates with Basis DSP*

## Key Steps
1. **Local OAuth Server**: Python script (`oauth_callback_server.py`) handles the callback.
2. **Token Generation**: Uses `authorization_code` flow (see code snippets below).
3. **Secure Storage**: Tokens encrypted in production (removed for demo).

## Code Highlights
```python
# Simplified OAuth callback handler
def do_GET(self):
    code = parse_qs(urlparse(self.path).get("code", [None])[0]
    print(f"Auth code received: {code}")  # In prod, exchange for token