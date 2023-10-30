import requests
from src.config.config import Config
from src.applications.github.api.github_api import GitHubAPI

def test_search_for_existing_repo():
    
    github_api_client = GitHubAPI
    existing_repo_name = 'sergii'
    repos = github_api_client.search_repos(existing_repo_name)

    assert repos['total_count'] != 0

def test_search_for_non_existing_repo():
    
    github_api_client = GitHubAPI
    non_existing_repo_name = 'lkjkjhg'
    repos = github_api_client.search_repos(non_existing_repo_name)

    assert repos['total_count'] == 0


# -s

