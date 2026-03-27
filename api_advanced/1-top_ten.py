#!/usr/bin/python3
"""Function that queries Reddit API and prints top 10 hot posts"""
import json
import urllib.error
import urllib.request


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    opener = urllib.request.build_opener(urllib.request.HTTPHandler)
    opener.addheaders = [
        ('User-Agent', 'linux:myredditapp:v1.0 (by /u/GabbyIT-pixel)')
    ]
    urllib.request.install_opener(opener)

    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req, timeout=10)
        if response.geturl() != url:
            print(None)
            return
        data = json.loads(response.read().decode('utf-8'))
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except urllib.error.HTTPError:
        print(None)
    except urllib.error.URLError:
        print(None)
