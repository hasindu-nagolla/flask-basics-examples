# Flask Basics Practice Repo

This repository is arranged as a numbered learning path. Each folder contains one small Flask example, and the folder number shows the order a beginner can follow.

## Learning Path

1. [01-home-route](01-home-route)
2. [02-route-variable](02-route-variable)
3. [03-url-building-redirect](03-url-building-redirect)
4. [04-methods-and-form-data](04-methods-and-form-data)

## What Each Example Teaches

- `01-home-route/app.py`: a first Flask app with the home route
- `02-route-variable/app.py`: dynamic route parameters
- `03-url-building-redirect/app.py`: `url_for()` and redirects
- `04-methods-and-form-data/app.py`: GET vs POST and form/query data
- `04-methods-and-form-data/templates/login.html`: HTML form page for testing GET and POST

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

Run the example you want by pointing Python at the file inside the folder:

```bash
python 01-home-route/app.py
python 02-route-variable/app.py
python 03-url-building-redirect/app.py
python 04-methods-and-form-data/app.py
```

Open your browser at `http://127.0.0.1:5000/`.

For the methods example, open `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/login` and use the form to submit a name with GET or POST.

## GitHub Push

From this project folder:

```bash
git add .
git commit -m "Organize Flask examples into numbered folders"
git push
```

If you want a new repo from scratch next time, GitHub CLI can create and push it in one step:

```bash
gh repo create <repo-name> --public --source=. --remote=origin --push
```
