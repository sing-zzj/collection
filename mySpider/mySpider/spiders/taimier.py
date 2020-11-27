import scrapy

with open('C:/Users/Administrator/Desktop/dicts/dicts_s.txt', encoding='utf-8') as fp:
    words = fp.read()
all_words = words.split('\n')
all_words[0] = 'ABC'

class TaimierSpider(scrapy.Spider):
    name = 'taimier'
    allowed_domains = ['en.glosbe.com']
    start_urls = ['https://en.glosbe.com/en/ta/{}?page=1&tmmode=MUST'.format(word) for word in all_words[9220:9350]]
    # start_urls = ['https://en.glosbe.com/en/ta/this?page=1&tmmode=MUST',
    #               'https://en.glosbe.com/en/ta/that?page=1&tmmode=MUST']

    print(start_urls)

    def parse(self, response):

        divs = response.xpath("//div[@id='tmTable']/div")
        ens = []
        tas = []
        i = 0
        for div in divs:
            en = div.xpath('.//div[@lang="en"]//text()').extract()[1:]
            ta = div.xpath('.//div[@lang="ta"]//text()').extract()[2:]
            en = ''.join(en)
            ta = ''.join(ta)
            print(str(i) + '.' + en)
            print(str(i) + '.' + ta)
            i += 1
            ens.append(en)
            tas.append(ta)

        with open('en.txt', 'a', encoding='utf-8') as pf:
            pf.write('\n'.join(ens))
            pf.write('\n')
        with open('ta.txt', 'a', encoding='utf-8') as ne:
            ne.write('\n'.join(tas))
            ne.write('\n')

        sign = response.xpath('//div[@id="tm-tab-cont"]/center[@class="muted"]/span/text()').extract()
        if len(sign) == 0:
            next_page = response.xpath('//div[@class="pagination"]//li/a[@rel="next nofollow"]/@href').extract_first()
            next_page = response.urljoin(next_page)
            yield scrapy.Request(
                next_page,
                callback=self.parse
            )