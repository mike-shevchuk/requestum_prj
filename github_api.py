import requests


GITHUB_TOKEN = None

USER_EVENTS_THAT_MAKE_A_CONTRIBUTION = {
        'PushEvent', 'PullRequestEvent', 'PullRequestReviewCommentEvent'
}
PER_PAGE = 100


def _call_github_api(url: str):
    page = 1
    res = []
    while True:
        req = requests.get(url,
                           params={'per_page': PER_PAGE, 'page': page},
                           headers={
                              'Accept': 'application/vnd.github.v3+json',
                              'Authorization': 'Bearer ' + GITHUB_TOKEN,
                              'X-GitHub-Api-Version': '2022-11-28',
                           })
        assert req.status_code == 200, f'Error: {req.text}'
        res.extend(req.json())
        if 'next' in req.links:
            page += 1
        else:
            break
    return res


def get_contributors(owner: str, repo: str):
    res = _call_github_api(f'https://api.github.com/repos/{owner}/{repo}/contributors')
    return [r['login'] for r in res if r['type'] == 'User']


def get_user_contributions(user: str):
    res = _call_github_api(f'https://api.github.com/users/{user}/events')
    return set(r['repo']['name'] for r in res if r['type'] in USER_EVENTS_THAT_MAKE_A_CONTRIBUTION)
