import requests
from bs4 import BeautifulSoup
import json
import logging

# Configure logging
logging.basicConfig(
    filename="blog_scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
BASE_URL = "https://sahibulsaif.wordpress.com/"

EXCLUDED_LINKS = {
    "https://wordpress.com/start?ref=wplogin",
    "https://sahibulsaif.wordpress.com/wp-login.php",
    "https://sahibulsaif.wordpress.com/feed/",
    "https://sahibulsaif.wordpress.com/comments/feed/",
    "https://wordpress.com/"
}

OUTPUT_FILE = "blog_data.json"

def fetch_page(url):
    """Fetches the page content and returns a BeautifulSoup object."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        logging.error(f"Failed to fetch {url}: {e}")
        return None

def get_archive_links():
    """Extracts archive links from the main page."""
    soup = fetch_page(BASE_URL)
    if not soup:
        return []
    
    widget_area = soup.find('li', class_='widget-container widget_archive')
    if not widget_area:
        logging.warning("No archive widget found.")
        return []
    
    return [a['href'] for a in widget_area.find_all('a') if a['href'] not in EXCLUDED_LINKS]

def get_blog_links(archive_links):
    """Extracts blog post links from archive pages."""
    blog_links = []
    for link in archive_links:
        soup = fetch_page(link)
        if not soup:
            continue
        found_links = [a['href'] for a in soup.select('h2.entry-title a')]
        blog_links.extend(found_links)
    return blog_links

def scrape_blog_post(blog_url):
    """Extracts blog details from an individual post."""
    soup = fetch_page(blog_url)
    if not soup:
        return None
    
    return {
        "title": soup.find('h2', class_='entry-title').get_text(strip=True) if soup.find('h2', class_='entry-title') else "No Title",
        "url": blog_url,
        "date": soup.find('span', class_='entry-date').get_text(strip=True) if soup.find('span', class_='entry-date') else "No Date",
        "author": soup.find('span', class_='author vcard').get_text(strip=True) if soup.find('span', class_='author vcard') else "No Author",
        "content": "\n".join([p.get_text(strip=True) for p in soup.find_all('div', class_='entry-content')]) if soup.find('div', class_='entry-content') else "No Content"
    }



def main():
    logging.info("Starting blog scraper.")
    archive_links = get_archive_links()
    blog_links = get_blog_links(archive_links)
    
    blog_data = []
    for blog_url in blog_links:
        logging.info(f"Scraping: {blog_url}")
        blog_post = scrape_blog_post(blog_url)
        if blog_post:
            blog_data.append(blog_post)
    
    if blog_data:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(blog_data, f, indent=4, ensure_ascii=False)
        logging.info(f"Scraped data saved to {OUTPUT_FILE}")
    else:
        logging.warning("No blog data scraped.")
    
    logging.info("Scraper finished execution.")


# Runs the Full Script
if __name__ == "__main__":
    main()