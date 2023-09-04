#!/usr/bin/python3
"""
takes GitHub credentials(username and password)
uses GitHub API to display id
use Basic Authentiction with a personal access token as passwd
"""

if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) == 3:
        username = sys.argv[1]
        passwd = sys.argv[2]
    url = "https://api.github.com/user"
    auth = (username, passwd)

    try:
        res = requests.get(url, auth=auth)
        if res.status_code == 200:
            data = res.json()
            user_id = data.get("id")
            print(user_id)
        else:
            print("Request failed: {}".format(res.status_code))
    except requests.exceptions.RequestException as e:
        print("Request Error: {}".format(e))
