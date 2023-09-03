#!/usr/bin/python3
"""
takes in a url
sends  request to the url
display body of response
manage urllib.error.HTTPError
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print("URL error: {}".format(e))
