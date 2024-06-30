#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Construct the URL for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent header to avoid rate limiting
    headers = {
        'User-Agent': 'Python script for fetching subreddit subscribers (by /u/yourusername)'
    }
    
    try:
        # Send a GET request to Reddit API
        response = requests.get(url, headers=headers)
        
        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            
            # Extract number of subscribers
            subscribers = data['data']['subscribers']
            
            return subscribers
        else:
            # Handle unsuccessful request
            print(f"Failed to fetch data for subreddit '{subreddit}'. Status code: {response.status_code}")
            return 0
        
    except Exception as e:
        # Handle any exceptions
        print(f"An error occurred: {str(e)}")
        return 0
