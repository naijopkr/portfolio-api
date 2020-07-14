from fetch_projects import fetch_projects
import requests as req
import json

# user = 'naijopkr'
# url = f'https://api.github.com/users/{user}/repos?type=owner&sort=updated&per_page=100'


url = 'https://rickandmortyapi.com/graphql'
query = """query {
    characters {
        results {
            name
            status
            species
            type
            gender
        }
    }
}
"""
res = req.post(url, json={'query': query})
