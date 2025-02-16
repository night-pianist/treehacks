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


        # full_url = response.urljoin(state_links[0])
        # yield scrapy.Request(url=full_url, callback=self.get_state_name)

    def get_state_name(self, response): # get all the states from the home page
        # You can process each individual state page here
        state = response.css('h1::text').get()
        state_name = state.split()[0]

        # job_details = response.css('div.job-listings')  # Modify this based on the actual page structure
       
        energy_efficiency_job_link = response.xpath(f'//a[contains(text(), "{state_name} Energy Efficiency Jobs")]/@href').get()

        print(f"HEREEEEEEEEE state is {state_name}")
        print(f"energy_efficiency_job_link URL for energy efficiency job link: {energy_efficiency_job_link}")

        if energy_efficiency_job_link:
            full_url = response.urljoin(energy_efficiency_job_link)
            print(f"full_url: {full_url}")
            yield scrapy.Request(
                url=full_url, 
                callback=self.parse_individual_state_energy_page,
                meta={'location': state_name}
            )

        # yield {
        #     'state': state_name,
        # }

    def parse_individual_state_energy_page(self, response): # get the individual job page from the energy jobs
        titles = response.css("li.job dd.title strong a::text").getall()

        for title in titles:
            yield {
                'title': title.strip(),
                'industry': "Energy",
                'location': response.meta['location'],
            }

        # for title in titles:
        #     yield {
        #         'title': title,
        #         'industry': "Energy",
        #         'location': response.meta['state_name'],
        #     }

      