import praw
from utils.dotenv_loader import load_env


class RedditFetcher:
    """
    Connect to Reddit using the PRAW library.
    Fetch posts from the subreddit specified
    by the user (e.g., the "hot" posts).
    """
    def __init__(self):
        client_id, client_secret, user_agent = load_env()
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

    def fetch_posts(self, subreddit_name, limit):
        subreddit = self.reddit.subreddit(subreddit_name)
        return list(subreddit.hot(limit=limit))
