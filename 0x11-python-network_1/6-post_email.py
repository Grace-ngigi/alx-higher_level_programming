#!/usr/bin/python3
"""
takes in url and email
sends a post request
display the body
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    req = requests.post(url, email)
    print(req.text)
