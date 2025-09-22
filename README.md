# GitHub Code Insights API

A FastAPI-based microservice that connects to the GitHub API to provide insights into repositories, commits, pull requests, and contributors.  
It uses [PyGithub](https://pygithub.readthedocs.io/) under the hood and is containerized with Docker for easy deployment.

---

## 🚀 Features
- **Recent Commits** → Get metadata on latest commits (author, date, lines added/deleted, files changed).  
- **Pull Requests** → List open/closed/all PRs with details (author, changes, additions, deletions).  
- **Contributors** → Fetch contributors with commit counts.  
- **Commit Files** → View file-level details for a specific commit.  
- **Commit Stats** → Get summary of additions, deletions, and changes in a commit.  

---

## 📂 Project Structure
```
.
├── Dockerfile
├── main.py
├── requirements.txt
```

- **Dockerfile** → Container setup for FastAPI app with Uvicorn.  
- **main.py** → FastAPI application exposing GitHub insights endpoints.  
- **requirements.txt** → Python dependencies.  

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2️⃣ Install Dependencies (Local Run)
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Environment Variables
```bash
export GITHUB_TOKEN=your_personal_access_token
export OWNER=your_org_or_user
export REPO=your_repository
```

### 4️⃣ Run Locally
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

The API will be available at:  
👉 [http://localhost:8080/docs](http://localhost:8080/docs) (Swagger UI)

---

## 🐳 Run with Docker

### Build Image
```bash
docker build -t github-code-insights .
```

### Run Container
```bash
docker run -d -p 8080:8080 \
  -e GITHUB_TOKEN=your_token \
  -e OWNER=your_org_or_user \
  -e REPO=your_repository \
  github-code-insights
```

---

## 📖 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/commits?limit=5` | GET | Get latest commits (default limit = 5) |
| `/prs?state=open` | GET | List pull requests (`open`, `closed`, `all`) |
| `/contributors` | GET | List repo contributors with commit count |
| `/commit/{sha}/files` | GET | Get files changed in a commit |
| `/commit/{sha}/stats` | GET | Get commit statistics (additions, deletions, changes) |

---

## 🔑 Authentication
This service uses a **GitHub Personal Access Token (PAT)** via environment variable `GITHUB_TOKEN`.  
Generate one at [GitHub Developer Settings → Tokens](https://github.com/settings/tokens).

---

## 🛠️ Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/) – Web framework  
- [Uvicorn](https://www.uvicorn.org/) – ASGI server  
- [PyGithub](https://pygithub.readthedocs.io/) – GitHub API client  
- [Docker](https://www.docker.com/) – Containerization  

---

## 📌 Example Request
```bash
curl "http://localhost:8080/commits?limit=3"
```

Response:
```json
{
  "commits": [
    {
      "sha": "abc123",
      "author": "octocat",
      "date": "2025-09-21T12:34:56Z",
      "message": "Fix bug in API",
      "files_changed": 2,
      "lines_added": 12,
      "lines_deleted": 4
    }
  ]
}
```

---

## 📜 License
MIT License – free to use, modify, and distribute.
