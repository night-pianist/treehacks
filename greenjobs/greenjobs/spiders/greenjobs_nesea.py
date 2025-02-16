import scrapy

class GreenJobsNeseaSpider(scrapy.Spider):
    name = "nesea" # use this name to run it
    start_urls = [
        'https://nesea.org/jobs-board/all-jobs',
    ]

    def parse(self, response):
        for row in response.css('tr'):  # Loop through each job row
            job_title = row.css('td.views-field-title h3 a::text').get()  # Extract job title from h3
            location = row.css('td.views-field-field-job-location::text').get()  # Extract location

            job_description = row.css('td.views-field-title::text').getall()
            # Clean up and get the job description
            cleaned_job_description = " ".join([text.strip() for text in job_description if text.strip()])
            description_lower = cleaned_job_description.lower()

            if job_title and location and 'energy' in (description_lower or job_title.lower()):
                yield {
                    'title': job_title.strip() if job_title else '',
                    'location': location.strip() if location else ''
                }
        # Find the 'next' page link
        next_page = response.css('li.pager-next a::attr(href)').get()

        # If the 'next' page exists, make a request to it
        if next_page:
            yield response.follow(next_page, self.parse)
