import requests as req
import json

def map_projects(repo):
    print(repo)
    if not repo.get('fork'):
        return dict(
            id=repo['id'],
            name=repo['name']
        )

def fetch_projects():
    user = 'naijopkr'
    url = f'https://api.github.com/users/{user}/repos?type=owner&sort=updated&per_page=100'

    try:
        res = req.get(url)
        projects = json.loads(res.text)
        repos = filter(lambda x:x, map(map_projects, projects))
        return list(repos)
    except Exception as e:
        print(e)
        return []
