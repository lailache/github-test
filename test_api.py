import os

import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

base_url = 'https://api.github.com'


def create_repo():
    url = f'{base_url}/user/repos'
    data = {
        'name': REPO_NAME,
        'private': False
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f'Repository {REPO_NAME} created successfully.')
    else:
        print(f'Failed to create repository: {response.json()}')


def check_repo_exists():
    url = f'{base_url}/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f'Repository {REPO_NAME} exists.')
    else:
        print(f'Repository {REPO_NAME} does not exist.')


def delete_repo():
    url = f'{base_url}/repos/{GITHUB_USERNAME}/{REPO_NAME}'
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f'Repository {REPO_NAME} deleted successfully.')
    else:
        print(f'Failed to delete repository: {response.json()}')


if __name__ == '__main__':
    create_repo()
    check_repo_exists()
    delete_repo()
    check_repo_exists()
