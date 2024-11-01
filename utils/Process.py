from bs4 import BeautifulSoup
from utils import HTMLCollector
from utils import MetaCollector
from utils import TextCollector
from utils import HomePageScraper
import os
import requests
import datetime
from datetime import date
from htmldate import find_date

class Process:
    """Takes in a homepage URL then loops through the links on it, 'processing' each one"""

    def __init__(self, url):
        self.scraper = HomePageScraper.HomePageScraper(url)
        self.url_list = self.scraper.urls_to_list()

    def log_processed_url(self, url):
        """Save list of processed URLs to txt file in data/processed"""
        with open("./data/processed/processed.txt", "a") as file:
            file.write(url + '\n')

    def make_soup_object(self, page):
        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    def make_thread_directory(self, id):
        """Creates a new folder to associate with the thread being processed"""
        thread_folder_path = "./data/" + id
        os.makedirs(thread_folder_path, exist_ok=True)

    def make_scan_directory(self, id):
        scan_path = "/" + datetime.today().strftime('%Y-%m-%dT%H:%M:%S')
        os.makedirs("./data/" + id +"/" + scan_path,exist_ok = True)

    def check_thread_id(self, id):
        if(os.path.exists("./data/" + id )):
            return True
        else: 
            return False
        
    def check_scan(self, page):
        """Return True if the most recent scan is not up-to-date, False if it's up-to-date"""
        update_date = find_date(
            # Assigns update_date to the update date of page (the page being checked)
            page.content,
            extensive_search=False,
            original_date=False,
            outputformat="%Y-%m-%d %H:%M:%S",
        )
        
        # previous_update_date = https://stackoverflow.com/questions/54491156/validate-json-data-using-python
            # Look at the thread directory, look at most recent scan folder, check json metadata update date

        if update_date is previous_update_date:
            return False
        else:
            return True

    def process_current_list(self):
        """For each URL in the list, get thread HTML, metadata JSON, and content JSON"""

        for url in self.url_list:
            # Gets page from URL and makes a new directory for the thread
            page = requests.get(url, stream=True)  
            soup = self.make_soup_object(page)
            
            intro_element = soup.find(class_="intro")
            
            if intro_element is not None:
                id = intro_element.get("id")
                if self.check_thread_id(id): # return true if no thread ID folder
                    self.make_thread_directory(id)
                if self.check_scan(page): # return true if not-up-to-date
                    self.make_scan_directory(id)
                    
                    # HTML file
                    thread = HTMLCollector(soup, self.thread_folder_path)
                    (thread.saveHTML())

                    # JSON metadata file
                    meta = MetaCollector(page, soup, self.thread_folder_path)
                    (meta.meta_dump())

                    # JSON thread content file
                    content = TextCollector(soup, self.thread_folder_path)
                    (content.write_thread())

                    # Add URL to list of processed URLs
                    self.log_processed_url(url)

            


                threadNumber = intro_element.get("id")
                self.make_thread_directory(threadNumber)


            