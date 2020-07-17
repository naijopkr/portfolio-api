import requests as req
import json
import os

from utils import get_prop

BLACK_LIST = [
    'css-positions-training',
    'open-quizz-api',
    'open-quizz-web',
    'islr-labs'
]

def map_topics(topic: dict):
    return get_prop(['topic', 'name'], topic)


def map_projects(repo: dict):
    if (repo.get('isFork') or repo.get('name') in BLACK_LIST):
        return None

    language = get_prop(['primaryLanguage', 'name'], repo)
    topics = list(map(
        map_topics,
        get_prop(['repositoryTopics', 'nodes'], repo)
    ))

    return dict(
        id = repo.get('id'),
        name = repo.get('name'),
        publlished_on = dict(github = repo.get('url')),
        description = repo.get('description'),
        language = language,
        topics = topics,
        updated_at = repo.get('updatedAt')
    )

def fetch_projects():
    token = os.getenv('GITHUB_TOKEN')
    url = 'https://api.github.com/graphql'
    query = """query {
        viewer {
            repositories (first: 100, orderBy: { field: CREATED_AT, direction: DESC }) {
                nodes {
                    databaseId
                    id
                    name
                    description
                    isFork
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
