import scrapy
from ..items import ScrapmeShopItem

class ScrapmeSpider(scrapy.Spider):
    name = "scrapme_shop"
    page_number = 2
    start_urls = [
        "https://scrapeme.live/shop/page/1/"
    ]

    def parse(self, response):
        items = ScrapmeShopItem()
        all_products = response.css(".woocommerce-loop-product__link")

        for product in all_products:
            product_name = product.css(".woocommerce-loop-product__title::text").extract_first()
            product_price = product.css(".amount::text").extract_first()
            product_imagelink =  product.css(".wp-post-image::attr(src)").extract_first()

            items["product_name"] = product_name
            items["product_price"] = product_price
            items["product_imagelink"] = product_imagelink
        
            yield items

        next_page = "https://scrapeme.live/shop/page/" + str(ScrapmeSpider.page_number) + "/"
        if ScrapmeSpider.page_number < 49:
            ScrapmeSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
