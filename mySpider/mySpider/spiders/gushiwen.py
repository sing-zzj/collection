import scrapy

from mySpider.items import MyspiderItem

class GushiwenSpider(scrapy.Spider):
	name = 'gushiwen'
	allowed_domains = ['gushiwen.cn']
	start_urls = ['https://www.gushiwen.cn/default_1.aspx']

	def parse(self, response):

		div_list = response.xpath('//div[@class="left"]/div[@class="sons"]')
		for div in div_list:
			titles = div.xpath('.//b/text()').extract_first()
			author = div.xpath('.//p[@class="source"]//text()').extract()
			contents = div.xpath('.//div[@class="contson"]//text()').extract()
			contents = ''.join(contents).strip()
			# poem = {}
			item = MyspiderItem()
			if titles != None:
				item["标题"] = titles
				item["作者"] = author
				item["内容"] = contents
				yield item
				# print(poem)

		href = response.xpath('//div[@class="pagesright"]/a[@id="amore"]/@href').extract_first()

		try:
			if len(href) != 0:
				href = response.urljoin(href)
				yield scrapy.Request(
					href,
					callback=self.parse,
				)
		except:
			pass
