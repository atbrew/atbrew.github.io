#! python

import markdown2
import pdfkit
import argparse


def markdown_to_pdf(markdown_file_path):
    # Extract the file name without the extension
    file_name = markdown_file_path.rsplit('.', 1)[0]

    # Convert the Markdown file to HTML
    with open(markdown_file_path, 'r') as md_file:
        markdown_text = md_file.read()
        html_text = markdown2.markdown(markdown_text)

    # Convert the HTML to a PDF file
    pdfkit.from_string(html_text, file_name + '.pdf')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a Markdown file to a PDF.')
    parser.add_argument('--input', '-i', required=True, help='The Markdown file to convert.')

    args = parser.parse_args()

    markdown_to_pdf(args.input)
