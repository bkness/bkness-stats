import json
import os
from datetime import datetime

import requests

OWNER = "bkness"
TOKEN = os.environ["STATS_TOKEN"]
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json",
}


def gh_api(path, params=None):
    url = f"https://api.github.com{path}"
    response = requests.get(url, headers=HEADERS, params=params or {})
    response.raise_for_status()
    return response.json()


def list_repos(visibility):
    repos = []
    page = 1

    while True:
        data = gh_api(
            f"/users/{OWNER}/repos",
            {"visibility": visibility, "per_page": 100, "page": page},
        )
        if not data:
            break

        repos.extend(data)
        page += 1

    return [repo["name"] for repo in repos]


def count_open_issues(repo):
    data = gh_api(
        "/search/issues",
        {"q": f"repo:{OWNER}/{repo} is:issue is:open", "per_page": 1},
    )
    return data["total_count"]


def main():
    repos = list_repos("public") + list_repos("private")
    total_issues = sum(count_open_issues(repo) for repo in repos)

    result = {
        "total_issues": total_issues,
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }

    with open("total-issues.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()