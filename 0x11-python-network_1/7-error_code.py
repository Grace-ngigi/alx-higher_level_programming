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

    try:
        res = requests.get(url)
        if res.status_code >= 400:
            print("Error code: {}".format(res.status_code))
        else:
            print(res.text)
    except requests.exceptions.RequestException as e:
        print("Request error: {}".format(e))
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
