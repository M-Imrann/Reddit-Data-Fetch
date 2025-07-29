import unittest
from unittest.mock import MagicMock, patch
from export_data import CSVExporter, PDFExporter


class TestExportData(unittest.TestCase):
    """
    Test Class to test the csv and pdf exporter classes.
    """
    def test_csv_exporter(self):
        """
        Test case to test the csv Exporter class.
        """
        posts = [MagicMock(title="Test Post 1", score=10)]
        csv_exporter = CSVExporter()

        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            csv_exporter.export(posts)
            mock_file.assert_called_once_with('output/posts.csv',
                                              mode='w',
                                              newline='',
                                              encoding='utf-8')

    def test_pdf_exporter(self):
        """
        Test case to test the pdf Exporter class.
        """
        posts = [MagicMock(title="Test Post 1", score=10)]
        pdf_exporter = PDFExporter()
        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            pdf_exporter.export(posts)
            mock_file.assert_called_once_with('output/posts.pdf', 'wb')


if __name__ == '__main__':
    unittest.main()
