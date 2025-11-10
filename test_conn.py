# test_conn.py
import httpx, sys, os

# Force IPv4 by using 127.0.0.1 explicitly
url = "http://127.0.0.1:11434/"

try:
    r = httpx.get(url, timeout=10.0)
    print("STATUS", r.status_code)
    print(r.text)
except Exception as e:
    print("ERROR:", type(e).__name__, e)
    sys.exit(1)
