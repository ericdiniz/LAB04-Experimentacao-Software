import requests
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json"
}
GRAPHQL_URL = "https://api.github.com/graphql"

def readQuery(after_cursor=None):
    with open("src/githubQuery.gql", "r", encoding="utf-8") as file:
        base_query = file.read()
    after = f', after: "{after_cursor}"' if after_cursor else ""
    return { "query": base_query.replace("{AFTER}", after) }

def fetchRepositories(total=1000):
    repos = []
    cursor = None
    while len(repos) < total:
        response = requests.post(GRAPHQL_URL, headers=HEADERS, json=readQuery(cursor))
        if response.status_code != 200:
            print("Erro:", response.text)
            break
        data = response.json()["data"]["search"]
        for repo in data["nodes"]:
            repos.append({
                "name": repo["name"],
                "owner": repo["owner"]["login"],
                "language": repo["primaryLanguage"]["name"] if repo["primaryLanguage"] else "Unknown",
                "stars": repo["stargazerCount"],
                "forks": repo["forkCount"],
                "createdAt": repo["createdAt"],
                "updatedAt": repo["updatedAt"],
                "license": repo["licenseInfo"]["name"] if repo["licenseInfo"] else "No license",
                "topics": ", ".join([t["topic"]["name"] for t in repo["repositoryTopics"]["nodes"]]),
                "description": repo["description"] or ""
            })
        if not data["pageInfo"]["hasNextPage"]:
            break
        cursor = data["pageInfo"]["endCursor"]
    return repos[:total]
