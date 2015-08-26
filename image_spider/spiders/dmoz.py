# coding = utf-8
__author__ = 'zsh'

import scrapy


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["http://www.hexun.com/"]
    start_urls = [
        "http://tech.hexun.com/2015-08-26/178619693.html",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-3] + ".html"
        print "has catch", filename
        with open(filename, 'wb') as f:
            f.write(response.body)
