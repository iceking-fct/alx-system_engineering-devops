#!/usr/bin/python3
import requests
import sys

if len(sys.argv) < 2:
    print("argument needed")
    sys.exit(1)


hdrs = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0"
}
url = f"https://www.reddit.com/r/{sys.argv[1]}/about.json"
print(f"Subreddit: {sys.argv[1]}:\nurl: {url}")
response = requests.get(url, headers=hdrs,
                        allow_redirects=False)
stat = response.status_code
print(f"response code: {stat}")

if stat != 200:
    sys.exit(1)

try:
    res_data = response.json()
    if res_data["data"]:
        print(res_data["data"]["subscribers"])
    else:
        print(0)
except Exception as e:
    print(res_data.keys())
    print(f"something failed: {str(e)}")
