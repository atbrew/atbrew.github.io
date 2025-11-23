#! python

import markdown2
import pdfkit
import argparse
import os

def markdown_to_pdf(markdown_file_path, css_file_path=None):
    # Extract the file name without the extension
    file_name = markdown_file_path.rsplit('.', 1)[0]

    # Convert the Markdown file to HTML
    with open(markdown_file_path, 'r') as md_file:
        markdown_text = md_file.read()
        
        # Remove YAML front matter (content between --- delimiters at the start)
        if markdown_text.startswith('---'):
            # Find the closing --- delimiter
            end_of_frontmatter = markdown_text.find('\n---\n', 3)
            if end_of_frontmatter != -1:
                # Skip past the closing --- and newline
                markdown_text = markdown_text[end_of_frontmatter + 5:]
        
        # Remove the first <hr/> or <hr> tag if present
        markdown_text = markdown_text.replace('<hr/>', '', 1).replace('<hr>', '', 1)
        
        html_text = markdown2.markdown(markdown_text)

    # Read CSS content from all files in the specified directory
    css_content = ""
    if css_file_path:
        with open(css_file_path, 'r') as css_file:
            css_content = css_file.read()
        if css_content:
            print("CSS content loaded from :", css_file_path)
            print(css_content)
    else:
        css_content = """
            body {
                font-family: Arial, sans-serif;
                font-size: 12pt;
            }
            h1 {
                font-size: 24pt;
                color: #333;
                border-bottom: 2px solid #ccc;
            }
            h2 {
                font-size: 20pt;
                color: #444;
                border-bottom: 1px solid #ccc;
            }
            h3 {
                font-size: 18pt;
                color: #555;
            }
            p {
                margin-bottom: 15px;
            }
        """
        print("Using default CSS styles")

    # Create a temporary HTML file with embedded CSS
    html_file_path = file_name + '.html'
    with open(html_file_path, 'w') as html_file:
        html_file.write(f'''
        <html>
        <head>
            <style>
                {css_content}
            </style>
        </head>
        <body>
            {html_text}
        </body>
        </html>
        ''')

    # Convert the HTML file to a PDF file with additional options
    options = {
        'quiet': '',
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'no-outline': None,
        'encoding': "UTF-8",
        'enable-local-file-access': None
    }

    pdfkit.from_file(html_file_path, file_name + '.pdf', options=options)

    # Optionally, remove the temporary HTML file after conversion
    os.remove(html_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert a Markdown file to a PDF with optional custom styles.')
    parser.add_argument('--input', '-i', required=True, help='The Markdown file to convert.')
    parser.add_argument('--css', '-c', help='The CSS files for styling (optional).')

    args = parser.parse_args()

    markdown_to_pdf(args.input, args.css)