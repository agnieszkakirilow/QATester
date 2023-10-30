import requests
import src.config.config

class GitHubAPI:
    """Current class contains every API call we use in tests"""
    def __init__(self) -> None:
        pass

    def search_repos(repo_name):
        URL = src.config.config.config_all.get("URL")
        print(f'sending request to URL: {URL}')
        response = requests.get(URL, params={'q':repo_name})
        
        body = response.json()

        print(f'response retrieved: {body}')
        
        return body
    
    def search_commits(self, commit_hash):
        response = requests.get("https://api.github.com/search/repositories", params={'q':commit_hash})
        print(f'sent request to {response}')
        body = response.json(0)
        print(f'response retrieved: {body}')
        return body