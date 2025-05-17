import csv

def saveToCsv(repos, fileName="githubRepos.csv"):
    if not repos:
        return
    with open(fileName, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=repos[0].keys())
        writer.writeheader()
        writer.writerows(repos)
    print(f"Saved {len(repos)} repos to {fileName}")
