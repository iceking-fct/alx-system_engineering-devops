# 100-count.py
import requests

def count_words(subreddit, word_list):
    """ A function that queries the Reddit API and counts occurrences
        of each word in the word_list in the titles of the first 10 hot posts.
    """
    hdrs = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json"
    }
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    try:
        response = requests.get(url, headers=hdrs, allow_redirects=False)
        if response.status_code == 200:
            resdata = response.json()
            if resdata.get("data") and resdata["data"].get("children"):
                posts = resdata["data"]["children"]
                word_count = {word.lower(): 0 for word in word_list}
                for post in posts:
                    title = post["data"]["title"].lower()
                    for word in word_list:
                        word_count[word.lower()] += title.split().count(word.lower())
                for word, count in word_count.items():
                    if count > 0:
                        print(f"{word}: {count}")
            else:
                print(None)
        else:
            print(None)
    except Exception:
        print(None)
