#!/usr/bin/python3

import requests
import sys

def list_commits(repo_name, owner_name):
    """
    Retrieves and lists the most recent commits from a specified GitHub repository.

    Args:
        repo_name (str): The name of the repository.
        owner_name (str): The owner (user or organization) of the repository.

    Returns:
        None: Prints commit information in the format: "<sha>: <author name>".
    """
    # Construct the API URL
    api_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    
    # Send the request to the GitHub API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        commits = response.json()
        
        # Iterate over the first 10 commits and print them
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
    else:
        print(f"Failed to retrieve commits. Status code: {response.status_code}")

# Take the repository name and owner name from command line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# Call the function with the provided arguments
list_commits(repo_name, owner_name)
