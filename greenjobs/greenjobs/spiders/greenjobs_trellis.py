import scrapy

class GreenJobsTrellisSpider(scrapy.Spider):
    name = "greenjobstrellis" # use this name to run it
    start_urls = [
        'https://jobs.trellis.net/',
    ]

    def parse(self, response):
        # Step 1: Extract all the job links from the job listing page
        job_links = response.css('a.job-post-summary::attr(href)').getall()
        print(f"job_links: {job_links[0]}")
        
        # # Follow each job link
        # for job_link in job_links:
        #     # Use scrapy's `response.follow` to visit each job detail page
        #     yield response.follow(job_link, self.parse_job)

        yield response.follow(job_links[0], self.parse_job)

    def parse_job(self, response):
        # Step 2: Extract the desired details from the individual job page
        job_title = response.css('h1.job-post-details__title::text').get().strip()
        location = response.css('h2 + p::text').get().strip()

        job_description = response.css('div.job-description::text').get()
        cleaned_job_description = " ".join([text.strip() for text in job_description if text.strip()])
        description_lower = cleaned_job_description.lower()
        
        if job_title and location and "energy" in description_lower or "energy" in job_title.lower():
            yield {
                'title': job_title.strip() if job_title else 'N/A',
                'location': location.strip() if location else 'N/A',
            }