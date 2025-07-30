import unittest
from unittest.mock import patch
import os
from utils.dotenv_loader import load_env


class TestDotenvLoader(unittest.TestCase):
    """
    Test class to test the dotenv_loader.
    """
    @patch.dict(os.environ, {
        'REDDIT_CLIENT_ID': 'id',
        'REDDIT_CLIENT_SECRET': 'secret',
        'USER_AGENT': 'agent'
    })
    def test_load_env(self):
        client_id, secret, agent = load_env()
        self.assertEqual(client_id, 'id')
        self.assertEqual(secret, 'secret')
        self.assertEqual(agent, 'agent')


if __name__ == '__main__':
    unittest.main()
