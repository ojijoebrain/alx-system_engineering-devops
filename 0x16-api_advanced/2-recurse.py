#!/usr/bin/python3
"""
A script with a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    A recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    """
    res = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )

    if res.status_code == 200:
        for get_list in res.json().get("data").get("children"):
            data = get_list.get("data")
            title = data.get("title")
            hot_list.append(title)
        after = res.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
