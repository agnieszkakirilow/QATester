import pytest
from src.applications.github.api.github_api import GitHubAPI

@pytest.fixture
def git_hub_api_app():  # scope session etc.
    # before each test
    # pre test steps
    github_api_client = GitHubAPI
    yield github_api_client

    # post steps, i.e. remove user, won't be executed after assert, after test steps