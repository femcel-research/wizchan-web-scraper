import json
from bs4 import BeautifulSoup
from utils import HTMLCollector
from utils import MetaCollector
from utils import TextCollector
from utils import HomePageScraper
import os
import requests
import datetime
import logging
from datetime import datetime
from htmldate import find_date
from string import Template

class Process:
    """Takes in a homepage URL then loops through the links on it, 'processing' each one"""
    THREAD_META_PATH = Template("./data/$t/thread_meta_$t.json")  # $t for thread id
    THREAD_FOLDER_PATH = Template("./data/$t")  # $t for thread id
    SCAN_FOLDER_PATH = Template("./data/$t/" + datetime.today().strftime("%Y-%m-%dT%H:%M:%S"))  # $t for thread id

    def __init__(self, url):
        # Logging
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(
            filename=("./data/logs/" + datetime.today().strftime('%Y-%m-%dT%H:%M:%S') + ".log"),
            filemode="w",
            format=(datetime.today().strftime('%Y-%m-%dT%H:%M:%S') + " %(levelname)s: %(message)s"),
            style="%",
            level=logging.INFO
        )

        # Get URLs
        self.scraper = HomePageScraper.HomePageScraper(url)
        self.url_list = self.scraper.urls_to_list()

        # Log message 
        if (len(self.url_list) <= 0):
            logging.critical("URL list is empty")
        else: 
            logging.info("The following URLs have been scraped")
            for url in self.url_list:
                logging.info(url)

    def log_processed_url(self, url):
        """Save list of processed URLs to txt file in data/processed"""
        with open("./data/processed/processed.txt", "a") as file:
            file.write(url + '\n')

    def make_soup_object(self, page):  # TODO: Can probably delete when make_thread_initial_meta is reworked
        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    def make_thread_meta(self, page, id):  # TODO: Rework depending on what meta file it is
        """Calls the same meta_dump() that's used for each scan, using INITIAL_META_PATH"""
        meta = MetaCollector(page, self.make_soup_object(page), self.THREAD_FOLDER_PATH.substitute(t = id), True)
        (meta.meta_dump(True))
        # Maybe make call an overloaded dump method? Then have a separate method to update just the thread update_date
        
    def make_scan_files(self, page, soup, url, id):
        # JSON thread metadata file
        os.makedirs(self.SCAN_FOLDER_PATH.substitute(t = id), exist_ok = True)  # Make scan @ current time folder

        # HTML current scan file
        thread = HTMLCollector(soup, self.SCAN_FOLDER_PATH.substitute(t = id))
        (thread.saveHTML())

        # JSON current scan metadata file
        meta = MetaCollector(page, soup, self.SCAN_FOLDER_PATH.substitute(t = id), False)
        (meta.meta_dump(False))

        # JSON current scan thread content file
        content = TextCollector(soup, self.SCAN_FOLDER_PATH.substitute(t = id))
        (content.write_thread())

        self.make_thread_meta(page, id)

        # Add URL to list of processed URLs
        self.log_processed_url(url)

        logging.info("Generated scan for thread #" + id + "; added to processed.txt")  # Log message

    def check_thread_folder(self, id):
        """Return True if a folder for the specified ID exists"""
        if(os.path.exists(self.THREAD_FOLDER_PATH.substitute(t = id))):
            logging.info("A thread folder for thread #" + id + " exists")
            return True
        else: 
            return False
        
    def check_thread_meta(self, id):
        """Return True if an initial_meta file for the specified ID exists"""
        if(os.path.exists(self.THREAD_META_PATH.substitute(t = id))):
           logging.info("An initial_meta_" + id + ".json exists for thread #" + id)
           return True
        else:
            return False    

    def check_date_updated(self, page, id):
        """Return True if update_date in initial_meta matches current update_date"""
        with open(self.THREAD_META_PATH.substitute(t = id)) as json_file:
            data = json.load(json_file)
        
        previous_update_date = datetime.strptime(data["date_updated"], "%Y-%m-%dT%H:%M:%S")
        update_date = find_date(
            # Assigns update_date to the update date of page (the page being checked)
            page.content,
            extensive_search=False,
            original_date=False,
            outputformat="%Y-%m-%dT%H:%M:%S",
        )
        update_date = datetime.strptime(update_date, "%Y-%m-%dT%H:%M:%S")

        # Log message
        logging.info("Current update date for " + id + ": " + str(update_date))
        logging.info("Previous update date for " + id + ": " + str(previous_update_date))

        if update_date == previous_update_date:
            logging.info("Match means NO folder!")  # Log message
            return True
        else:
            logging.info("No match means FOLDER!")  # Log message
            return False

    def process_current_list(self):
        """For each URL in the list, get thread HTML, metadata JSON, and content JSON"""
        logging.info("Processing the URLs")  # Log message

        for url in self.url_list:
            # Gets page from URL and makes a new directory for the thread
            logging.info("Processing " + url)  # Log message
            page = requests.get(url, stream=True)  
            soup = self.make_soup_object(page)
            intro_element = soup.find(class_="intro")
            
            # Using intro_element since requests.get would still technically return a page, the page itself would just have a 404 error?
            # Tries to retrieve the id of the intro elem. If unable, it will log the specific status code of the page. Otherwise, continue as normal.
            # If at any point, a 404 slips through the cracks, retrieve code for stuff below committed prior to (11/19 6:15pm)
            try:
               id = intro_element.get("id") 
            except:
                logging.warning(page.status_code + " error; processing unsuccessful; skipping")  # Log message
            else:
                logging.info("Checking against previous scans")  # Log message
                if not self.check_thread_folder(id):  # return True if there is a thread ID folder
                    os.makedirs(self.THREAD_FOLDER_PATH.substitute(t = id), exist_ok=True)  # if False, make thread ID folder
                if not self.check_thread_meta(id):  # return True if there is an initial_meta file for the thread
                    self.make_scan_files(page, soup, url, id)
                else: 
                    if not self.check_date_updated(page, id):  # return True if previous scan up-to-date
                        self.make_scan_files(page, soup, url, id)  # if False, then scan normally
        
        logging.info("Fully processed all URLs") # Log message

                    


            