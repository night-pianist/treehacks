import scrapy

class GreenJobsStatesSpider(scrapy.Spider):
    name = "greenjobsstates" # use this name to run it
    start_urls = [
        'https://greenjobs.net/states/',
    ]

    def parse(self, response): # main parsing function
        state_links = response.css('ul li a::attr(href)').getall()
        for state in state_links:
            full_url = response.urljoin(state)
            yield scrapy.Request(url=full_url, callback=self.get_state_name)

    def get_state_name(self, response): # get all the states from the home page
        # You can process each individual state page here
        state = response.css('h1::text').get()  # Assuming the title of the page is in h1
        # job_details = response.css('div.job-listings')  # Modify this based on the actual page structure
       
        energy_efficiency_job_link = response.xpath(f'//a[contains(text(), "{state} Energy Efficiency Jobs")]/@href').get()

        if energy_efficiency_job_link:
            full_url = response.urljoin(energy_efficiency_job_link)
            yield scrapy.Request(url=full_url, callback=self.parse_individual_state_energy_pages, meta = {
                'state': state,
            }),
            

        # yield {
        #     'state': state,
        # }

    def parse_individual_state_energy_page(self, response): # get the individual job page from the energy jobs
        job_titles = response.css('dd strong::text').getall()

        for job_title in job_titles:
            yield {
                'state': response.meta['state'],
                'job_title': job_title,
            }



        
    # # def get_energy_jobs(self, response): # get the energy jobs from the individual state pages
    # #     energy_efficiency_job_link = response.xpath('//a[contains(text(), "Energy Efficiency Jobs")]/@href').get()

    # #     if energy_efficiency_job_link:
    # #         full_url = response.urljoin(energy_efficiency_job_link)
    # #         yield scrapy.Request(url=full_url, callback=self.parse_individual_job_page)
        
    




       