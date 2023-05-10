#!/usr/bin/python3
"""Defines number_of_subscribers()."""
import requests


def number_of_subscribers(subreddit):
    "Gets the number of subs of a subreddit."
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 \
        Safari/537.36'
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    return 0
