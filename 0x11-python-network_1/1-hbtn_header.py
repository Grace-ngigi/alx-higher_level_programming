#!/usr/bin/python3
"""send req and display value pf X-Requiest-Id"""

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
            print(dict(res.headers).get("X-Request-Id"))
    except urllib.error.URLEror as e:
        print(f"Error: {e}")
    
