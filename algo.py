from collections import defaultdict

import github_api


def get_most_similar_repos(user: str, repo: str, n: int = 5):
    contributors = github_api.get_contributors(user, repo)
    repo_contributors = defaultdict(list)
    for c in contributors:
        for r in github_api.get_user_contributions(c):
            if r != f'{user}/{repo}':
                repo_contributors[r].append(c)

    res = list(repo_contributors.items())
    res.sort(key=lambda repo_contributors: len(repo_contributors[1]), reverse=True)
    return res[:n]
