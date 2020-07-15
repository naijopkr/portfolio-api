import requests as req
import json

from utils import get_prop

def map_topics(topic: dict):
    return get_prop(['topic', 'name'], topic)


def map_projects(repo: dict):
    language = get_prop(['primaryLanguage', 'name'], repo)
    topics = list(map(
        map_topics,
        get_prop(['repositoryTopics', 'nodes'], repo)
    ))

    return dict(
        id = repo.get('id'),
        name = repo.get('name'),
        publlished_on = dict(github = repo.get('url')),
        language = language,
        topics = topics,
        updated_at = repo.get('updated_at')
    )

def fetch_projects():
    token = '3f3b718fe7b4ab69451836d7b8fac85023afc19c'
    url = 'https://api.github.com/graphql'
    query = """query {
    viewer {
        repositories (first: 100, orderBy: { field: CREATED_AT, direction: DESC }) {
        nodes {
            databaseId
            id
            name
            description
            url
            updatedAt
            primaryLanguage {
            name
            }
            repositoryTopics(first: 5) {
            nodes {
                topic {
                name
                }
            }
            }
        }
        }
    }
    }"""

    res = req.post(
        url,
        json={'query': query},
        headers={'Authorization': f'bearer {token}'}
    )

    projects_list = get_prop(
        ['data', 'viewer', 'repositories', 'nodes'],
        json.loads(res.text)
    )

    if not projects_list:
        return []

    return list(map(map_projects, projects_list))
