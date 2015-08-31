# coding = utf-8
__author__ = 'zsh'

import scrapy


class DmozSpider(scrapy.Spider):
    name = "pic"
    allowed_domains = ['https://www.reddit.com/']
    start_urls = [
        "https://www.reddit.com/r/pics",
    ]


    def parse(self, response):
        print response.url
        filename = response.url.split("/")[-2] + ".html"
        print "has catch", filename
        with open(filename, 'wb') as f:
            f.write(response.body)
