import os
import csv
from fpdf import FPDF


class CSVExporter:
    """
    Write the filtered posts to a CSV file using Python's built-in
    `csv` module. Include fields such as title, score, and URL
    """
    def __init__(self, filename='output/posts.csv'):
        self.filename = filename

    def export(self, posts):
        os.makedirs("output",
                    exist_ok=True
                    )
        with open(self.filename,
                  mode='w',
                  newline='',
                  encoding='utf-8'
                  ) as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Score', 'URL'])
            for post in posts:
                writer.writerow([post.title,
                                 post.score,
                                 post.url])


class PDFExporter:
    """
    Create a PDF summary of the filtered posts using
    the FPDF library. Each post's title, score, URL
    and other related data should be included in the PDF.
    """
    def __init__(self, filename='output/posts.pdf'):
        self.filename = filename

    def export(self, posts):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for post in posts:
            pdf.multi_cell(0,
                           10,
                           f"Title: {post.title}"
                           f"\nScore: {post.score}"
                           f"\nURL: {post.url}\n",
                           border=0
                           )
            pdf.ln(5)

        pdf.output(self.filename)
