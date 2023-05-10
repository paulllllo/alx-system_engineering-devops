#!/usr/bin/python3
"""Defines top_ten()."""
import requests


def top_ten(subreddit):
    """Gets the top 10 listings of a subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 \
        Safari/537.36'
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        for listing in res.json()['data']['children']:
            print(listing['data']['title'])
    else:
        print(None)
