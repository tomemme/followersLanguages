import requests

def get_followers(username, token):
    url = f"https://api.github.com/users/{username}/followers"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_languages(username, token):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    repos = response.json()
    languages = [repo['language'] for repo in repos if repo['language']]
    return languages
