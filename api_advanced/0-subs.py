#!/usr/bin/python3
"""Function that queries Reddit API and returns number of subscribers"""
import json
import urllib.request


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = urllib.request.Request(url)
    req.add_header(
        'User-Agent', 'linux:myredditapp:v1.0 (by /u/GabbyIT-pixel)'
    )
    try:
        response = urllib.request.urlopen(req, timeout=10)
        data = json.loads(response.read().decode('utf-8'))
        return data.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
