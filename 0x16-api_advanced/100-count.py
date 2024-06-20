#!/usr/bin/python3
"""
A script wiht a recursive function that queries the Reddit API, parses the
title of all hot articles, and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict={}):
    """
    A recursive function that queries the Reddit API, parses the
    title of all hot articles, and prints a sorted count of given keywords
    """
    if not word_list or word_list == [] or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if response.status_code != 200:
        return

    data = res.json()
    children = data["data"]["children"]

    for child in children:
        title = child["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                count_dict[word] = count_dict.get(word, 0)
                + title.count(word.lower())

    after = data["data"]["after"]
    if after:
        count_words(subreddit, word_list, after, count_dict)
    else:
        sorted_counts = sorted(count_dict.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
