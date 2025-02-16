import scrapy

class GreenJobsNewieeSpider(scrapy.Spider):
    name = "newiee" # use this name to run it
    start_urls = [
        'https://newiee.org/jobs-board/',
    ]

    def parse(self, response):
        for row in response.css('table#jobs-board tbody tr'):
            job_title = row.css('td.align-left a::text').get()  # Extract job title text
            category = row.css('td:nth-child(2)::text').get()
            employer = row.css('td:nth-child(3) a::text').get()
            location = row.css('td:nth-child(4)::text').get()  

            combined_text = f"{job_title} {category} {employer} {location}".lower()

            if 'energy' in combined_text:
                yield {
                    'title': job_title,
                    'location': location.strip() if location else ''
                }

            
            # yield {
            #     'Job Title': job_title,
            #     'Category': category.strip() if category else '',
            #     'Employer': employer.strip() if employer else '',
            #     'Location': location.strip() if location else ''
            # }



