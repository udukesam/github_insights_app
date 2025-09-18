from fastapi import FastAPI
from github import Github, Auth
import os

# ------------------------------
# Initialize FastAPI app
app = FastAPI(title="GitHub Code Insights API", version="1.0.0")

# Read environment variables at startup
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
OWNER = os.environ.get("OWNER")
REPO = os.environ.get("REPO")
REPO_NAME = f"{OWNER}/{REPO}" if OWNER and REPO else None

# Initialize GitHub auth (safe, lightweight)
auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

# ------------------------------
# GitHub API helper functions

def get_repo_object():
    """Fetch the repo object inside endpoint to avoid slow startup."""
    if not REPO_NAME:
        raise ValueError("OWNER or REPO environment variable is not set")
    return g.get_repo(REPO_NAME)

def recent_commits(limit=5):
    repo = get_repo_object()
    commits_data = []
    for count, commit_summary in enumerate(repo.get_commits()):
        if count >= limit:
            break
        commit = repo.get_commit(commit_summary.sha)
        files = list(commit.files or [])
        commits_data.append({
            "sha": commit.sha,
            "author": commit.commit.author.name,
            "date": commit.commit.author.date,
            "message": commit.commit.message,
            "files_changed": len(files),
            "lines_added": sum(f.additions for f in files),
            "lines_deleted": sum(f.deletions for f in files)
        })
    return commits_data

def list_prs(state="open"):
    repo = get_repo_object()
    prs_data = []
    for pr in repo.get_pulls(state=state):
        prs_data.append({
            "id": pr.id,
            "title": pr.title,
            "author": pr.user.login,
            "created_at": pr.created_at,
            "changed_files": pr.changed_files,
            "additions": pr.additions,
            "deletions": pr.deletions
        })
    return prs_data

def contributors_stats():
    repo = get_repo_object()
    return [{"login": c.login, "commits": c.contributions} for c in repo.get_contributors()]

def commit_files(sha):
    repo = get_repo_object()
    commit = repo.get_commit(sha)
    files = list(commit.files or [])
    return [{"filename": f.filename, "status": f.status, "additions": f.additions, 
             "deletions": f.deletions, "changes": f.changes} for f in files]

def commit_stats(sha):
    repo = get_repo_object()
    commit = repo.get_commit(sha)
    files = list(commit.files or [])
    return {
        "sha": commit.sha,
        "total_additions": sum(f.additions for f in files),
        "total_deletions": sum(f.deletions for f in files),
        "total_changes": sum(f.changes for f in files)
    }

# ------------------------------
# API endpoints

@app.get("/commits")
def get_commits(limit: int = 5):
    return {"commits": recent_commits(limit)}

@app.get("/prs")
def get_prs(state: str = "open"):
    return {"prs": list_prs(state)}

@app.get("/contributors")
def get_contributors():
    return {"contributors": contributors_stats()}

@app.get("/commit/{sha}/files")
def get_commit_files(sha: str):
    return {"commit": sha, "files": commit_files(sha)}

@app.get("/commit/{sha}/stats")
def get_commit_stats(sha: str):
    return commit_stats(sha)

if __name__ == "__main__":
    import uvicorn
    # Use the PORT environment variable provided by Code Engine
    port = int(os.environ.get("PORT", 8080))
    # Bind to 0.0.0.0 to be accessible from outside the container
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
