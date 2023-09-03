#!/usr/bin/python3
"""
takes in url
sends a request
display body response
if status code >= 400 print Error code
use packges request and sys
"""

if __name__ == "__main_":
    import sys
    import requests

    url = sys.argv[1]

    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
