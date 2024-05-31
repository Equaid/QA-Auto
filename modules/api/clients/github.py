import requests

class GitHub:

    def __init__(self):
        self.api_git = "https://api.github.com"


    def get_user(self, username):
        r = requests.get(f'{self.api_git}/users/{username}')
        body = r.json()

        return body
    
    def searh_repo(self, name):
        r = requests.get(
            f"{self.api_git}/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
    
    def get_repos(self):
        r = requests.get(f'{self.api_git}/repositories')
        body = r.json()

        return body


    def get_emoji(self):
        r = requests.get(
            f'{self.api_git}/emojis')
        body = r.json()

        return body
    
    def get_commit(self,username, repos_name):
        r = requests.get(f'{self.api_git}/repos/{username}/{repos_name}/commits')
        body = r.json

        return body