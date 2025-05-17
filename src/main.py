from githubClient import fetchRepositories
from csvWriter import saveToCsv

def main():
    repos = fetchRepositories(total=1000)
    saveToCsv(repos)

if __name__ == "__main__":
    main()
