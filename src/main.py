from githubClient import fetchRepositories
from csvWriter import saveToCsv

def main():
    language = "Python"
    perPage = 50
    pages = 2

    repos = fetchRepositories(language=language, perPage=perPage, pages=pages)
    saveToCsv(repos)

if __name__ == "__main__":
    main()
