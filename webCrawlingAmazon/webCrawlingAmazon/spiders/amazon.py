import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    productSearch = 'iphone'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com.br/s?k={}'.format(productSearch)]

    def parse(self, response):
        for item in response.css('.a-color-base.a-text-normal'):
            yield {
                'product' : response.css('.a-color-base.a-text-normal::text').get(),
                'price' : response.css('.a-price-whole::text').get()
            }