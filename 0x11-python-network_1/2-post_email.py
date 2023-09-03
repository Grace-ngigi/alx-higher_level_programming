#!/usr/bin/python3
"""
takes URL and email
send post request
display the reponse decoded in utf-8
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(email).encode("ascii")
    try:

        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print("Error: {}".format(e))
