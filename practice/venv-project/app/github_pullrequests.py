import requests

def fetch_pull_requests(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        pull_requests = response.json()
        user_pr_count = {}
        for pr in pull_requests:
            user = pr['user']['login']
            if user in user_pr_count:
                user_pr_count[user] += 1
            else:
                user_pr_count[user] = 1
        
        for user, count in user_pr_count.items():
            print(f"User: {user}, PR Count: {count}")
    else:
        print(f"Failed to fetch pull requests: {response.status_code}")

if __name__ == "__main__":
    repo_owner = "kubernetes"
    repo_name = "kubernetes"
    fetch_pull_requests(repo_owner, repo_name)