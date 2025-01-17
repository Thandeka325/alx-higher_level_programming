#!/usr/bin/python3
"""
This script takes a repository name and an owner name as arguments
and uses the GitHub API to display the commits of the specified repo.
Each commit will show its SHA and the author's name.
"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for i in range(min(10, len(commits))):
            sha = commits[i].get('sha')
            author = commits[i].get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    else:
        print("Error: Unable to fetch commits")
