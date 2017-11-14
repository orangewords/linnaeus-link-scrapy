import scrapy
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Join

class LLPubs (scrapy.Spider):
	name = "linlinks"
	start_urls = [
		'http://www.linnaeuslink.org/records/record/4000',
	]

	def parse(self, response):
		for item in response.css('div#contentContainer'):
			yield {
				'soulsby': response.css('div.field.soulsbyNo .value span::text').extract_first(),
				'uniformtitle': response.css('div.field.uniformTitle .value span::text').extract_first(),
				'title': response.css('div.field.title .value span::text').extract_first(),
				'author':  response.css('div.field.author .value span::text').extract_first(),
				'publisher':  response.css('div.field.publisher .value span::text').extract_first(),
				'pubplace': response.css('div.field.placeOfPublication .value span::text').extract_first(),
				'pubyear': response.css('div.field.publishingYear .value span::text').extract_first(),
				'opac': ", ".join(response.css('div.field.localControlNo .value span::text').extract()),
				'digitalcopyurl': ", ".join(response.css('div#digitalLinks li a').xpath('@href').extract()),
#				'name': ", ".join(response.css('div#digitalLinks li a span::text').extract()),
				'org': ", ".join(response.css('div#tabs ul li a::text').extract()),
				}



