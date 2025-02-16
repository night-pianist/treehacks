import scrapy

class GreenJobsBoardSpider(scrapy.Spider):
    name = "greenjobsboard" # use this name to run it
    start_urls = [
        'https://www.greenjobsboard.us/jobboard/explore-jobs',
    ]

    def parse(self, response):
        for job in response.css("div.w-dyn-item"):
            try:
                title = job.css("div.paragraph-med::text").get()
                industry = job.css("div.filter-industry::text").get()
                location = job.css("div.job-meta-wrap div.job-meta-tag::text").getall()[:1]  # First meta field only

                link = job.css("a::attr(href)").get()
                
                if industry == "Energy" and link:
                    yield response.follow(link, self.parse_job_detail, meta={
                        'title': title.strip(),
                        'industry': industry.strip(),
                        'location': location[0].strip() if location else 'No location'
                    })

                    # state = response.follow(link, self.parse_job_detail)
                    # yield {
                    #     "title": title.strip(),
                    #     "industry": industry.strip(),
                    #     "location": state
                    # }

                # yield {
                    # "title": title.strip(),
                    # "industry": industry.strip(),
                    # "location": location[0].strip() if location else 'No location' 
                # }
            except Exception as e:
                self.log(f"Error parsing job: {e}")

    def parse_job_detail(self, response):
        # Extracting the state from the job detail page
        location_state = response.css("div.location-container h3.job-properties-text.location-text::text").get()

        # Yield the result with the state
        yield {
            'title': response.meta['title'],
            # 'industry': response.meta['industry'],
            'location': location_state.strip() if location_state else location[0].strip()
        }
