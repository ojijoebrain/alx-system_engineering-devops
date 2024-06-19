#!/usr/bin/python3
"""
Script that queries subscribers on Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return total num of subscribers on given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
