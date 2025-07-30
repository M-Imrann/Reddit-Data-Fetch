import praw
from utils.dotenv_loader import load_env


class RedditClient:
    """
    Singleton class that Ensures only one Reddit instance is created.
    """
    _instance = None
    _reddit = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RedditClient, cls).__new__(cls)
            client_id, client_secret, user_agent = load_env()
            cls._reddit = praw.Reddit(
                client_id=client_id,
                client_secret=client_secret,
                user_agent=user_agent
            )
        return cls._instance

    def get_reddit(self):
        return self._reddit


class RedditFetcher:
    """
    Uses RedditClient to fetch subreddit posts.
    """
    def __init__(self):
        self.reddit = RedditClient().get_reddit()

    def fetch_posts(self, subreddit_name, limit):
        subreddit = self.reddit.subreddit(subreddit_name)
        return list(subreddit.hot(limit=limit))
