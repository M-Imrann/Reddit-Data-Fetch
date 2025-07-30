import unittest
from unittest.mock import patch, MagicMock
import main


class TestMain(unittest.TestCase):
    """"
    Test class to test the main.
    """
    @patch('main.parse_args')
    @patch('main.RedditFetcher')
    @patch('main.FilterPost')
    @patch('main.PostGenerator')
    @patch('main.PostIterator')
    @patch('main.PostZipper')
    @patch('main.CSVExporter')
    @patch('main.PDFExporter')
    def test_main_execution(
        self, mock_pdf_exporter, mock_csv_exporter,
        mock_zipper, mock_iterator, mock_generator,
        mock_filter, mock_fetcher, mock_parse_args
    ):
        # Set up dummy args
        mock_parse_args.return_value.name = 'python'
        mock_parse_args.return_value.limit = 2
        mock_parse_args.return_value.score = 5.0

        # Mock Reddit posts
        mock_post = MagicMock(title="Post Title",
                              score=10,
                              url="http://example.com")
        mock_fetcher().fetch_posts.return_value = [mock_post]

        # Filter returns the same mock post
        mock_filter().filter_post.return_value = [mock_post]

        # Generator yields the post
        mock_generator().post_generator.return_value = iter([mock_post])

        # Iterator yields post
        mock_iterator.return_value = iter([mock_post])

        # Zipper returns title-url pairs
        mock_zipper().zip_title_url.return_value = [(mock_post.title,
                                                     mock_post.url)]

        # Call main function
        main.main()

        # Validate key function calls
        mock_fetcher().fetch_posts.assert_called_once_with('python', 2)
        mock_filter().filter_post.assert_called_once()
        mock_csv_exporter().export.assert_called_once()
        mock_pdf_exporter().export.assert_called_once()


if __name__ == '__main__':
    unittest.main()
