#!/usr/bin/python3
"""
Script that queries subscribers on a Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
    except ValueError:
        print("Error decoding JSON response")
        return 0


if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit: ")
    subscribers = number_of_subscribers(subreddit)
    print(f"Number of subscribers in r/{subreddit}: {subscribers}")
