#!/usr/bin/python3
"""fetches data from some url and display in tabular form"""
if __name__ == "__main__":

    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with urllib.request.urlopen(url) as res:
            data = res.read()
            print(f"Body response:")
            print(f"- type: {type(data)}")
            print(f"- content: {data}")
            print(f"{'-' * 30}")
    except urllib.error.URLError as e:
        print(f"Error: {e}")
