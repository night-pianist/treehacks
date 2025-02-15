import sys
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Add the parent directory to sys.path to allow imports from 'spiders'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from greenjobs_board_spider import GreenJobsBoardSpider
from greenjobs_states import GreenJobsStatesSpider

def run_spider():
    # Create a CrawlerProcess to run your spiders
    process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'greenjobs.json',
})


    # Run the spider
    # process.crawl(GreenJobsBoardSpider)
    process.crawl(GreenJobsStatesSpider)
    # Set output to the same JSON file (optional, if you want the output in JSON format)
    # process.settings.set('FEED_FORMAT', 'json')
    # process.settings.set('FEED_URI', 'greenjobs.json')

    # Start crawling
    process.start()

# Call the run_spider function to start the spider
if __name__ == "__main__":
    try:
        run_spider()
    except Exception as e:
        print(f"Error occurred while running the spider: {e}")
