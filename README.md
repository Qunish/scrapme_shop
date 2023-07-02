# ScrapMe Shop Scraper

This is a Python script that uses the Scrapy framework to scrape product information from the ScrapMe Shop website.

## Prerequisites

Before running this script, ensure that you have the following installed:

- Python 3.x
- Scrapy

You can install Scrapy using pip:

```sh
pip install scrapy
```

## Usage

1. Clone this repository or download the script file.

2. Navigate to the directory containing the script in your terminal.

3. Run the following command to start the scraper:

   ```sh
   scrapy crawl scrapme_shop
   ```

4. The script will start scraping the product information from the ScrapMe Shop website. The scraped data includes the product name, price, and image link.

5. The scraped data will be saved to the `items.json` file in the same directory.

## Customization

If you want to customize the script, you can modify the following variables in the `ScrapmeSpider` class:

- `name`: The name of the spider. You can change it to a more descriptive name if desired.
- `start_urls`: The URLs to start scraping from. You can add or modify the URLs to scrape different pages or collections.
- `page_number`: The initial page number to start scraping from. You can change it to start from a different page.
- `if ScrapmeSpider.page_number < 49`: The condition to control the number of pages to scrape. You can modify the number or change the condition to scrape more or fewer pages.

## Notes

- This script assumes that the website structure remains the same. If the structure of the ScrapMe Shop website changes, the script may need to be updated accordingly.

- Make sure to respect the website's terms of service and scraping policies.
