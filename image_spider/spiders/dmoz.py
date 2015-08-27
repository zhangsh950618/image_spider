# coding = utf-8
__author__ = 'zsh'

import scrapy


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    # allowed_domains = ["http://www.hao123.com/"]
    start_urls = [
        "http://www.hao123.com/",
    ]

    def parse(self, response):
        print response.url
        filename = response.url.split("/")[-2] + ".html"
        print "has catch", filename
        with open(filename, 'wb') as f:
            f.write(response.body)
