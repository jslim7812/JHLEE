import js2xml                                                                   
import scrapy                                                                   

class ExampleSpider(scrapy.Spider):                                             
    name = 'example'                                                            
    allowed_domains = ['amazon.com']                                            
    start_urls = ['https://www.amazon.com/dp/B01N068GIX?psc=1/']                

    def parse(self, response):                                                  
        item = dict()
        js = response.xpath("//script[contains(text(), 'register(\"ImageBlockATF\"')]/text()").extract_first()
        xml = js2xml.parse(js)                                                  
        selector = scrapy.Selector(root=xml)                                   
        item['image_urls'] = selector.xpath('//property[@name="colorImages"]//property[@name="hiRes"]/string/text()').extract()
        yield item

# exmple.py 있는 디렉토리로 이동, user_agent ="" 내용 변경 후 CMD 창에서 아래줄 
#scrapy runspider example.py -s USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
