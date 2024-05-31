import pytest



@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.searh_repo('become_qa_auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.searh_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_chare_be_found(github_api):
    r = github_api.searh_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
def test_get_repos(github_api):
    r = github_api.get_repos()
    assert isinstance(r, list)


@pytest.mark.api
def test_emoji(github_api):
    r = github_api.get_emoji()
    assert 'ambulance' in r
    assert isinstance(r, dict)

@pytest.mark.api
def test_get_commit(github_api):
    r = github_api.get_commit('octocat','Hello-World')
    assert isinstance(r, list)
