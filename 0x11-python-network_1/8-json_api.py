#!/usr/bin/python3
"""
takes in a leter
sends a post request to some url
with the letter as a prameter
response body is Json formatted
"""

if __name__ == "__main__":
    import sys
    import requests

    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    q = {"q": letter}

    try:
        res = requests.post(url, data=q)
        data = res.json()

        if data is not {}:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not  valid JSON")
    except requests.exceptions.RequestException as e:
        print("Request Error:", e)
