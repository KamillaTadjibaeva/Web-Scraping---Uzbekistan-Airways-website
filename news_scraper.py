import scrapy
from scrapy.crawler import CrawlerProcess

base_url = "https://www.uzairways.com/en/press-center/news"

process = CrawlerProcess(settings={
    'LOG_LEVEL': 'ERROR',
    'USER_AGENT': 'Student_project',
    'FEEDS': {
        'data/news_scrapy.json': {
            'format': 'json',
            'overwrite': True,
        },
    },
    'DOWNLOAD_DELAY': 1,
})

class NewsSpider(scrapy.Spider):
    name = 'news'
    start_urls = [base_url + '?page=' + str(i) for i in range(5)] #first 5 pages of news
    
    def parse(self, response):
        items = response.css('div.text-wrapper') #going through each text-wrapper classes on the page
        
        for item in items:
            title = item.css('h5.item-title a::text').get()
            link = item.css('h5.item-title a::attr(href)').get()
            date = item.css('div.publish-date time::text').get()
            
            if link:
                yield response.follow(
                    link,
                    callback=self.parse_article, # function to call when the page is downloaded
                    meta={ # data to pass along to that function
                        'title': title.strip() if title else '',
                        'date': date.strip() if date else '',
                    }
                )
    
    def parse_article(self, response):
        title = response.meta['title']
        date = response.meta['date']
        
        body_parts = response.css('div.news-single-content p::text').getall()
        body = ' '.join([p.strip() for p in body_parts if p.strip()])
        
        # extract image URLs from the article content
        image_srcs = response.css('div.news-single-content img::attr(src)').getall()
        #join base url scrapy is currently on with src
        image_urls = [response.urljoin(src) for src in image_srcs]
        
        yield {
            'title': title,
            'date': date,
            'url': response.url,
            'body': body,
            'image_urls': image_urls,
        }

process.crawl(NewsSpider) # Add the spider to the process to be run
process.start() # Start the crawling process
