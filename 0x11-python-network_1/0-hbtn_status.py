#!/usr/bin/python3
"""fetches data from some url and display in tabular form"""
if __name__ == "__main__":

    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with urllib.request.urlopen(url) as res:
            data = res.read()
            print(f"Body response:")
            print('\t- type: {}'.format(type(data)))
            print('\t- content: {}'.format(data))
            print('\t- utf8 content: {}'
                  .format(data.decode("utf-8", "replace")))
    except urllib.error.URLError as e:
        print(f"Error: {e}")
