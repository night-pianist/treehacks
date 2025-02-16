import sys
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Add the parent directory to sys.path to allow imports from 'spiders'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from greenjobs_board_spider import GreenJobsBoardSpider
from greenjobs_states import GreenJobsStatesSpider
from greenjobs_newiee import GreenJobsNewieeSpider
from greenjobs_nesea import GreenJobsNeseaSpider
from greenjobs_trellis import GreenJobsTrellisSpider

def run_spider():
    # Create a CrawlerProcess to run your spiders
    process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'TRELLIS.json',
})


    # Run the spider
    # process.crawl(GreenJobsBoardSpider)
    # process.crawl(GreenJobsStatesSpider)
    # process.crawl(GreenJobsNewieeSpider)
    # process.crawl(GreenJobsNeseaSpider)
    process.crawl(GreenJobsTrellisSpider)


    # Start crawling
    process.start()

# Call the run_spider function to start the spider
if __name__ == "__main__":
    try:
        run_spider()
    except Exception as e:
        print(f"Error occurred while running the spider: {e}")
