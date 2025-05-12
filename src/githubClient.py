import requests
import os
from dotenv import load_dotenv

load_dotenv()
githubToken = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {githubToken}",
    "Accept": "application/vnd.github+json"
}

def fetchRepositories(language="Python", perPage=50, pages=2):
    repos = []

    for page in range(1, pages + 1):
        url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc&per_page={perPage}&page={page}"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            continue

        data = response.json()
        for repo in data["items"]:
            repos.append({
                "name": repo["name"],
                "owner": repo["owner"]["login"],
                "language": repo["language"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "createdAt": repo["created_at"],
                "updatedAt": repo["updated_at"],
                "topics": ", ".join(repo.get("topics", [])),
                "license": repo["license"]["name"] if repo["license"] else "No license",
                "description": repo["description"] or ""
            })

    return repos
