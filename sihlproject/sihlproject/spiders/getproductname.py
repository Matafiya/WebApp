import scrapy


class QuotesSpider(scrapy.Spider):
    name = "productname"

    def start_requests(self):
        urls = [
            'https://www.sihl.com/en/products/productcategories/photo-papers/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for product in response.css('article.products-e2__row'):
            yield {
                'paper': product.css('a.products-e2__link::text').get(),
                'surface': product.css('section.products-e2__column--surface::text').get(),
                'infolink': product.css('a.products-e2__link::attr(href)').get()
            }