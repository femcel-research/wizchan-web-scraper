import json
from bs4 import BeautifulSoup
from utils import HTMLCollector
from utils import MetaCollector
from utils import TextCollector
from utils import HomePageScraper
import os
import requests
import datetime
from datetime import datetime
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

    def update_scan_data_file(self, page, path):
        meta = MetaCollector(page, self.make_soup_object(page), path)
        (meta.meta_dump())

    def make_soup_object(self, page):
        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    def make_thread_directory(self, id):
        """Creates a new folder to associate with the thread being processed"""
        thread_folder_path = "./data/" + id
        os.makedirs(thread_folder_path, exist_ok=True)

    def make_scan_directory(self, id):
        scan_path = "/" + datetime.today().strftime('%Y-%m-%dT%H:%M:%S')
        os.makedirs("./data/" + id + scan_path,exist_ok = True)
        return "./data/" + id +"/" + scan_path

    def check_thread_id(self, id):
        """Return True if a folder for the specified ID does NOT exist"""
        if(os.path.exists("./data/" + id )):
            return False
        else: 
            return True
        
    def check_scan(self, page, id):
        """Return True if the most recent scan is NOT up-to-date, False if it's up-to-date;
        makes a scan data JSON if it doesn't exist already"""
        # Check to see if there is a data file
        partial_data_path = "./data/" + id + "/"
        scan_data_path = "./data/" + id + "/" + "meta_" + id + ".json"
        if(os.path.exists(scan_data_path) == False):
            self.update_scan_data_file(page, partial_data_path)
            return True
        else:
            with open(scan_data_path) as json_file:
                data = json.load(json_file)
            previous_update_date = data["date updated"]

            update_date = find_date(
                # Assigns update_date to the update date of page (the page being checked)
                page.content,
                extensive_search=False,
                original_date=False,
                outputformat="%Y-%m-%d %H:%M:%S",
            )
            
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
                if self.check_thread_id(id): # return True if no thread ID folder
                    self.make_thread_directory(id)
                if self.check_scan(page, id): # return True if not-up-to-date
                    thread_folder_path = self.make_scan_directory(id)
                    
                    # HTML file
                    thread = HTMLCollector(soup, thread_folder_path)
                    (thread.saveHTML())

                    # JSON metadata file
                    meta = MetaCollector(page, soup, thread_folder_path)
                    (meta.meta_dump())

                    # JSON thread content file
                    content = TextCollector(soup, thread_folder_path)
                    (content.write_thread())

                    # Add URL to list of processed URLs
                    self.log_processed_url(url)
                    # self.update_scan_data_file(page)


            