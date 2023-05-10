#!/usr/bin/python3
"""Defines recurse()."""
import requests


def recurse(subreddit, hot_list=[]):
    """Gets all hot listings of a subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 \
        Safari/537.36'
    }
    params = {'after': None, 'limit': 100}
    if hot_list:
        params['after'] = hot_list[-1].get('data', None).get('name', None)
    res = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if res.status_code == 200:
        if res.json().get('data', None).get('children', None):
            hot_list.extend(res.json()['data']['children'])
            return recurse(subreddit, hot_list)
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return None
