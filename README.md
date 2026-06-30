# Books Catalog Scraper

Scrapes book listings from books.toscrape.com, a practice site built for 
learning web scraping, covering all 50 pages of the catalog.

## What it extracts
- Book title
- Star rating (One through Five)
- Price
- Stock availability

## Tools used
- Selenium — opens the site and loads each page
- BeautifulSoup — extracts title, rating, price, and availability from the HTML
- Pandas — combines all results and exports to Excel

## How it works
The scraper loops through all 50 catalog pages using the site's predictable 
URL pattern, collecting data from every book card on each page before 
combining everything into a single clean dataset.

## Output
1,000 rows (20 books × 50 pages) saved to a single Excel file, ready for delivery.

## Setup
pip install -r requirements.txt
