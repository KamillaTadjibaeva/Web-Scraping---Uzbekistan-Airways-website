Name: Kamilla Tadjibaeva
Student ID: 488381

FILES

1. project_report.ipynb  - Main Jupyter Notebook with the full project report
2. news_scraper.py - Scrapy spider script for news articles (run by the notebook as a subprocess)
3. data/ - Folder with all scraped data (CSV, JSON) and downloaded article images (data/images/)
4. requirements.txt - List of all required Python packages
5. legal_proof.txt - Written proof that scraping uzairways.com is legal
6. README.txt - This file

HOW TO RUN

1. Create a virtual environment and activate it:
   python -m venv .venv (alternatively use python3)
   source .venv/bin/activate (Mac)
   .venv\Scripts\activate (Windows)

2. Install the required packages:
   Make sure you are in the project root directoryand run:
   pip install -r requirements.txt

3. Open project_report.ipynb in Jupyter Notebook or VS Code and select the kernel with venv you just created

4. Run all cells one by one or Run All (the notebook creates the data/ folder automatically
   and runs news_scraper.py as a subprocess to scrape news articles)


NOTE

I intentionally enabled the automatic pop up of the chrome so that the user can see how the site buttons are being clicked. 
So do not be surprised when the chrome window pops up 2 times throughout the notebook.
Do not close them, just enjoy the buttons being clicked.
