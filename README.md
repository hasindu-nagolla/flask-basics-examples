# Flask Basics Practice Repo

This repository contains small Flask examples for learning core concepts:

- Basic app and home route
- Route variables
- URL building and redirecting

## Files

- `app_hello_world.py`: minimal Flask app with `/`
- `app_route_variable.py`: dynamic route using `/hello/<name>`
- `app_url_building_redirect.py`: route redirection using `url_for`

## Prerequisites

- Python 3.10+

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Examples

Run one file at a time:

```bash
python app_hello_world.py
```

Or:

```bash
python app_route_variable.py
python app_url_building_redirect.py
```

Open your browser at `http://127.0.0.1:5000/`.

## GitHub Push (New Repository)

From this project folder:

```bash
git init
git add .
git commit -m "Initial commit: Flask basics examples"
git branch -M main
```

Create a repo on GitHub and connect it:

```bash
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

If GitHub CLI is installed and authenticated, you can also do:

```bash
gh repo create new-project --public --source=. --remote=origin --push
```
