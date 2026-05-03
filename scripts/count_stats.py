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



def fetch_repos(visibility):
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

    return repos


def fetch_org_repos(visibility):
    repos = []
    page = 1

    while True:
        data = gh_api(
            f"/orgs/{OWNER}/repos",
            {"visibility": visibility, "per_page": 100, "page": page},
        )
        if not data:
            break

        repos.extend(data)
        page += 1

    return repos


def list_repos(visibility):
    try:
        return [repo["name"] for repo in fetch_repos(visibility)]
    except requests.HTTPError as exc:
        if exc.response.status_code in (403, 404):
            return [repo["name"] for repo in fetch_org_repos(visibility)]
        raise


def count_open_issues(repo):
    count = 0
    page = 1

    while True:
        issues = gh_api(
            f"/repos/{OWNER}/{repo}/issues",
            {"state": "open", "per_page": 100, "page": page},
        )
        if not issues:
            break

        count += sum(1 for issue in issues if "pull_request" not in issue)
        page += 1

    return count


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