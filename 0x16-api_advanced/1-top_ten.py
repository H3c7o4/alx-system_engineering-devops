#!/usr/bin/python3
"""
"""
import requests


def top_ten(subreddit):
    """
       Function that queries the Reddit API and prints the titles of
       the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    requests = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 200:
        for children in request.json().get("data").get("children"):
            print(children.get("data").get("title"))

    else:
        print(None)
