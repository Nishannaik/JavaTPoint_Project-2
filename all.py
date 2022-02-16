import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllSpider(CrawlSpider):
    name = 'all'
    allowed_domains = ['javatpoint.com']
    start_urls = ['https://www.javatpoint.com/data-warehouse']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='leftmenu']/a")), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='next'])[2]"))
    )

    def parse_item(self, response):
        yield {
       'Title': response.xpath("//h1[@class='h1']/text()").getall(),
       'All_H2_Subheadings': response.xpath("//h2[@class='h2']/text()").getall(),
       'All_H3': response.xpath("//h3[@class='h3']/text()").getall(),
       'All_para': response.xpath("//p/text()").getall(),
       'li': response.xpath("//ul/li/text()").getall(),
       'links': response.url,
       'section_links':response.xpath("//div[@class='leftmenu']/a/@href").getall(),
       'images_link': response.xpath("//img/@src").getall()
       

       #'images':response.xpath("//img[@class='imageright']/@src").extract.getall(),
       #'All_Links':response.xpath("//div[@class='firsthomecontent']/a").getall()
        }
