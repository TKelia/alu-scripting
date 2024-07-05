#!/usr/bin/python3
"""
Fetches the number of subscribers for a specified Reddit subreddit.
"""

import requests

def get_subscriber_count(subreddit):
    """ Fetches subscriber count from Reddit API """
    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    if 'data' not in data or 'subscribers' not in data['data']:
        return 0
    return data['data']['subscribers']
