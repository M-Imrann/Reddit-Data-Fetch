# Reddit Subreddit Post Fetcher

A Python script that fetches Reddit posts from any subreddit using PRAW, 
filters them based on score, and exports them to both CSV and PDF formats.
The script is fully modular, uses environment variables for credentials,
and follows Python best practices.

---

## Features

- 🔍 Fetches hot posts from a user-specified subreddit.
- ⚙️ Accepts command-line arguments for subreddit, post limit, and minimum score.
- 🔐 Uses environment variables for Reddit API credentials via `.env` file.
- ⚡ Filters posts using `filter` and `lambda` functions.
- 🌀 Implements both a generator function and a custom iterator class.
- 🔗 Uses `zip` and `lambda` to pair fields like title and URL.
- 🧾 Exports filtered posts to:
  - `output.csv`: using Python’s `csv` module.
  - `report.pdf`: using the `fpdf` library.

---

## Technologies Used

- Python
- [`praw`](https://praw.readthedocs.io/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)
- [`fpdf`](https://pyfpdf.github.io/)

---

## Installation

### 1. Clone the Repository

- ```bash
- git clone https://github.com/yourusername/reddit-fetcher.git
- cd reddit-fetcher


### 2. Create and Activate Virtual Environment

- python -m venv venv
#### Activate it:
- source venv/bin/activate      # On Linux/Mac
- venv\Scripts\activate         # On Windows


### 3. Install Required Packages

- pip install -r requirements.txt


### 4. Run the Script

- python main.py --subreddit <subreddit_name> [--limit <number>] [--min_score <score>]

#### Example

- python main.py --subreddit python --limit 15 --min_score 100
