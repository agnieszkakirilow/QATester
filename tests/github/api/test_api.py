from confitest import git_hub_api_app

def test_search_for_existing_repo(git_hub_api_app):

    # test steps
    existing_repo_name = 'sergii'
    repos = git_hub_api_app.search_repos(existing_repo_name)

    assert repos['total_count'] != 0

    
def test_search_for_non_existing_repo(git_hub_api_app):
    
    
    non_existing_repo_name = 'lkjkjhg'
    repos = git_hub_api_app.search_repos(non_existing_repo_name)

    assert repos['total_count'] == 0


# -s


