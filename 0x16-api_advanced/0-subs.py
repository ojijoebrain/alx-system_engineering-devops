#!/usr/bin/python3
"""
A script that queries the Reddit API and returns the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and
    returns the number of subscribers.
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        result = res.json()
        subscribers = result['data']['subscribers']
        return subscribers
    else:
        return 0
