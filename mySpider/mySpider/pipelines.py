# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

import pymysql

class MyspiderPipeline:

	def process_item(self, item, spider):

		item["内容"], item["作者"] = self.get_content(item["内容"], item["作者"])

		conn = pymysql.connect('localhost', 'root', 'root', 'poem')
		cursor = conn.cursor()
		sql = "INSERT INTO advice_poem values('{0}', '{1}', '{2}')".format(item["标题"], item["作者"], item["内容"])
		cursor.execute(sql)
		conn.commit()
		cursor.close()
		conn.close()

		return item

	def get_content(self, content, author):
		content = content.replace('\u3000', '').replace('\\n', '')
		author = ''.join(author)
		return content, author