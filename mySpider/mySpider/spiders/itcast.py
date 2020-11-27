import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
    	filename = 'teacher.txt'
    	print(response.text)
    	with open(filename, 'w') as pf:
    		pf.write(response.text)
    	# open(filename, 'w').write(response.text)
    
