#!/usr/bin/python3
"""Recursive function that counts keywords in hot articles titles"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Prints sorted count of given keywords in hot articles"""
    if after is None:
        word_count = {word.lower(): 0 for word in word_list}
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {"User-Agent": "linux:myredditapp:v1.0 (by /u/GabbyIT-pixel)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        after = data.get("data", {}).get("after", None)
        for post in posts:
            title = post.get("data", {}).get("title", "").lower().split()
            for word in title:
                if word in word_count:
                    word_count[word] += 1
        if after is not None:
            return count_words(subreddit, word_list, after, word_count)
        sorted_words = sorted(word_count.items(),
                              key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            if count > 0:
                print("{}: {}".format(word, count))
    return None
