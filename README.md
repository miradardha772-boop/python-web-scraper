# Simple Python Web Scraper

A lightweight Python automation tool that scrapes quotes and author names from a target website and exports the structured data directly into a clean CSV file. 

Built as a beginner portfolio project to demonstrate core Python programming, HTML parsing, and data persistence skills.

## 🚀 Features
* **Web Request Handling:** Uses the `requests` library to securely fetch HTML content from a target webpage.
* **HTML Parsing:** Leverages `BeautifulSoup` to search, filter, and extract specific text elements from the page structure.
* **Data Export:** Automatically organizes the scraped data and saves it locally into a structured `quotes.csv` file using Python's built-in `csv` module.

## 🛠️ Technologies Used
* **Python 3**
* **Requests** (HTTP library)
* **BeautifulSoup4** (HTML parsing)
* **CSV** (Data storage)

## ⚙️ How to Run Locally

1. Make sure you have Python installed.
2. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4
