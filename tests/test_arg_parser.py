import unittest
from unittest.mock import patch
from arg_parser import parse_args


class TestArgParser(unittest.TestCase):
    @patch('sys.argv',
           ['main.py', '--name', 'python', '--limit', '5', '--score', '10'])
    def test_parse_args(self):
        args = parse_args()
        self.assertEqual(args.name, 'python')
        self.assertEqual(args.limit, 5)
        self.assertEqual(args.score, 10.0)


if __name__ == '__main__':
    unittest.main()
