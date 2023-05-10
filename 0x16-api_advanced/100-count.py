#!/usr/bin/python3
"""Defines count_words()."""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Counts the number of times a set of words in all hot listings."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 \
        Safari/537.36'
    }
    params = {'after': after, 'limit': 100}
    res = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if res.status_code == 200:
        data = res.json().get('data', None).get('children', None)
        if data:
            for listing in data:
                for word in listing.get('data', {}).get('title', '')
                .lower().split(' '):
                    if word in word_list:
                        word_count[word] = word_count.get(word, 0) + 1
            if res.json()['data']['after']:
                return count_words(
                    subreddit,
                    word_list,
                    word_count,
                    res.json()['data']['after']
                )
        if word_count == {}:
            return print()
        for k, v in sorted(
            word_count.items(), key=lambda t: t[1], reverse=True
        ):
            print('{}: {}'.format(k, v))
    else:
        return print()
