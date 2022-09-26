import scrapy

class TopcvSpider(scrapy.Spider):
    name = 'topcv'
    start_urls = ['https://www.topcv.vn/tim-viec-lam-moi-nhat?sort=up_top']

    def parse(self, response):
        jobs = response.css('div.job-item.bg-highlight.job-ta.result-job-hover')
        for job in jobs:
            yield {
                'name':job.css('h3 span::text').get(),
                'company': job.css('p a::text').get(),
                'salary':job.css('label.salary::text').get(),
                'location':job.css('label.address::text').get(),
                'link':job.css('h3 a::attr(href)').get()
            }
        next_pgae = response.css('div.text-center a').attrib['href']
        if next_pgae is not None:
            yield response.follow(next_pgae, callback=self.parse)