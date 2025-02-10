# Web Scraper for Sahibulsaif Blog

## Overview
This Python script scrapes blog post data from [Sahibulsaif.wordpress.com](https://sahibulsaif.wordpress.com/). It extracts and saves information about each blog post, including:
- Blog Title
- Blog Author
- Blog Date
- Blog Content
- Blog URL

The extracted data is stored in a **JSON file** for easy access and analysis.

---

## Prerequisites
Before running the script, install the required Python libraries.

### Install Dependencies
Run the following command:
```sh
pip install beautifulsoup4 requests
```

### Libraries Used
- **BeautifulSoup4**: Parses HTML and extracts required elements.
- **Requests**: Sends HTTP requests to fetch web pages.
- **JSON** (built-in): Saves the extracted data in JSON format.

---

## How the Code Works

### **1. Extracting Archive Page Links**
The script first fetches **archive page links** from the homepage using the `widget-container widget_archive` class.

### **2. Extracting "Continue Reading" Links**
From each archive page, it extracts "Continue Reading" links using `h2.entry-title a` selectors.

### **3. Extracting Blog Post Data**
For each blog post URL, the script extracts:
- **Title** (`h2.entry-title`)
- **Date** (`span.entry-date`)
- **Author** (`span.author vcard`)
- **Content** (`div.entry-content p`)

### **4. Storing Data in JSON Format**
The extracted data is saved in `blog_data.json` in the following format:
```json
[
    {
        "title": "Know Your Limits",
        "url": "https://sahibulsaif.wordpress.com/2011/07/31/the-biggest-knowledge-is-to-know-your-limits/",
        "date": "July 31, 2011",
        "author": "sahibulsaif",
        "content": "Sohbet by Sheykh Abdul Kerim al-Hakkani al-Kibrisi..."
    }
]
```

---

## How to Run the Script
1. Clone or download the script.
   ```sh
   git clone https://github.com/abrarshahh/WebScraping_beautifulsoup.git
   ```
2. Install dependencies using:
   ```sh
   pip install beautifulsoup4 requests
   ```
3. Run the python script `scraping.py`
4. The extracted blog data will be saved in **blog_data.json**.

---

## Additional Notes
- The script **filters out unnecessary links** (e.g., login pages, feeds, etc.).
- If the website structure changes, **selectors may need to be updated**.
- To modify the output format, adjust the `json.dump` function.

---

## License
This script is open-source and can be used freely with modifications as needed.

---

Happy Scraping! 🚀

