#!/usr/bin/python3
"""
takes in a url
sends a request
display value of X=Request-Id
use requests package
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
