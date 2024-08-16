#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post["data"]["title"])

    except requests.RequestException:
        print(None)
    except Exception:
        print(None)

