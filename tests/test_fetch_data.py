import unittest
from unittest.mock import patch, MagicMock
from fetch_data import RedditFetcher


class TestFetchData(unittest.TestCase):
    """
    Test class to test the fetch posts.
    """
    @patch('fetch_data.praw.Reddit')
    @patch('utils.dotenv_loader.load_env',
           return_value=('id', 'secret', 'agent'))
    def test_fetch_posts(self, mock_env, mock_reddit):
        """
        Test case to test the fetch_posts function.
        """
        mock_post = MagicMock()
        mock_post.title = "Test"
        mock_post.score = 100
        mock_post.url = "http://example.com"

        mock_subreddit = MagicMock()
        mock_subreddit.hot.return_value = [mock_post]
        mock_reddit.return_value.subreddit.return_value = mock_subreddit

        fetcher = RedditFetcher()
        posts = fetcher.fetch_posts('test', 1)

        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].title, "Test")


if __name__ == '__main__':
    unittest.main()
