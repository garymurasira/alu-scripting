#!/usr/bin/python3
"""Recursive function that queries Reddit API and returns list of hot titles"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns list of titles of all hot articles for a given subreddit"""
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
            hot_list.append(post.get("data", {}).get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
