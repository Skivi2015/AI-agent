import os
import requests

GITHUB_REPOS = [
    "Skivi2015/AImanager-AIM",
    "Skivi2015/Omniscope",
    "Skivi2015/Godmode",
    "Skivi2015/AI-agent",
    "Skivi2015/android-ci-bootstrap"
]

class Plugin:
    def __init__(self, agent):
        self.agent = agent
        self.token = os.environ.get("GITHUB_TOKEN")

    def can_handle(self, cmd):
        return cmd.startswith("github")

    def handle(self, cmd):
        if "clone" in cmd:
            repo = cmd.split("clone", 1)[1].strip()
            if repo == "all":
                return self.clone_all()
            return self.clone_repo(repo)
        elif "list" in cmd:
            return self.list_repos()
        return "GitHub command not recognized."

    def clone_repo(self, repo):
        import subprocess
        try:
            result = subprocess.run(
                ["git", "clone", f"https://github.com/{repo}.git"], 
                capture_output=True, 
                text=True, 
                timeout=30
            )
            if result.returncode == 0:
                return f"Cloned repo {repo}"
            else:
                return f"Error cloning {repo}: {result.stderr}"
        except subprocess.TimeoutExpired:
            return f"Error cloning {repo}: Operation timed out"
        except Exception as e:
            return f"Error cloning {repo}: {e}"

    def clone_all(self):
        results = []
        for repo in GITHUB_REPOS:
            results.append(self.clone_repo(repo))
        return "\n".join(results)

    def list_repos(self):
        if not self.token:
            return "GitHub token not set."
        url = "https://api.github.com/user/repos"
        headers = {"Authorization": f"token {self.token}"}
        resp = requests.get(url, headers=headers)
        if resp.ok:
            repos = [r["full_name"] for r in resp.json()]
            return "\n".join(repos)
        return f"Error: {resp.text}"