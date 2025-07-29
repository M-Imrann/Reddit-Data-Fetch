import unittest
from data_processing import FilterPost, PostGenerator, PostIterator, PostZipper
from unittest.mock import MagicMock


class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        self.posts = [
            MagicMock(title="Post1", score=15, url="url1"),
            MagicMock(title="Post2", score=5, url="url2")
        ]

    def test_filter_post(self):
        """
        Test case to test the filter post class.
        """
        filtered = FilterPost(10).filter_post(self.posts)
        self.assertEqual(len(filtered), 1)

    def test_post_generator(self):
        """
        Test case to test the Post Generator class.
        """
        gen = PostGenerator(self.posts).post_generator()
        self.assertEqual(len(list(gen)), 2)

    def test_post_iterator(self):
        """
        Test case to test the Post Iterator class.
        """
        iterated = list(PostIterator(self.posts))
        self.assertEqual(len(iterated), 2)

    def test_post_zipper(self):
        """
        Test case to test the Post Zipper class.
        """
        zipped = PostZipper(self.posts).zip_title_url()
        self.assertEqual(zipped[0][0], "Post1")
        self.assertEqual(zipped[0][1], "url1")


if __name__ == '__main__':
    unittest.main()
