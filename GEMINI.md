# Project Overview

This is a personal website and blog built with Jekyll, a static site generator. The site is hosted on GitHub Pages. The project also includes Python scripts for various utility tasks, such as converting Markdown files to PDFs and processing images.

## Building and Running

### Jekyll Site

To build and serve the Jekyll site locally, use the following command from the `docs` directory:

```bash
bundle exec jekyll serve
```

This will start a local web server at `http://localhost:4000`.

### Python Scripts

The Python dependencies are managed with Poetry. To install the dependencies, run:

```bash
poetry install
```

The Python scripts are located in the `src` directory. They are intended to be run as standalone scripts. For example, to convert a Markdown file to PDF:

```bash
python src/convert_markdown_to_pdf_in_place.py --input <path_to_markdown_file> --css <path_to_css_file>
```

To remove the background from an image:

```bash
python src/remove_background.py
```

## Development Conventions

### Jekyll

The Jekyll site uses the `bay_jekyll_theme`. The site's configuration is in `docs/_config.yml`. Blog posts are written in Markdown and are located in the `docs/_posts` directory.

### Python

The Python code uses standard libraries and dependencies listed in `pyproject.toml`. The scripts are designed for command-line usage.

## GitHub Actions Build Pipeline

The project uses GitHub Actions for continuous deployment to GitHub Pages. The workflow is defined in `.github/workflows/jekyll-gh-pages.yml` and is triggered on pushes to the `main` branch or manually via `workflow_dispatch`.

The pipeline performs the following steps:

1.  **Checkout:** Checks out the repository.
2.  **Set up Node.js:** Configures Node.js version 16.
3.  **Install Roboto:** Installs the `@fontsource/roboto` npm package.
4.  **Setup Python:** Configures Python version 3.x.
5.  **Install wkhtmltopdf:** Installs `wkhtmltopdf` which is required for PDF generation.
6.  **Install Dependencies:** Installs Python dependencies (`markdown2`, `pdfkit`) using pip.
7.  **Convert CV to PDF:** Runs the `src/convert_markdown_to_pdf_in_place.py` script to convert `docs/cv.markdown` to a PDF.
8.  **Setup Ruby:** Configures Ruby version 3.1.4 and installs Ruby gems using `bundler`.
9.  **Setup Pages:** Configures the GitHub Pages environment.
10. **Build with Jekyll:** Builds the Jekyll site in the `docs` directory, setting the `baseurl` and `JEKYLL_ENV` to production.
11. **Upload artifacts:** Uploads the built site (`./docs/_site`) as an artifact.
12. **Deploy to GitHub Pages:** Deploys the uploaded artifact to GitHub Pages.
