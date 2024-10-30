from bs4 import BeautifulSoup
from utils import HTMLCollector
from utils import MetaCollector
from utils import TextCollector
from utils import HomePageScraper
import os
import requests

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
        self.thread_folder_path = "./data/" + id
        os.makedirs(self.thread_folder_path, exist_ok=True)

    def process_current_list(self):
        """For each URL in the list, get thread HTML, metadata JSON, and content JSON"""

        for url in self.url_list:
            # Gets page from URL and makes a new directory for the thread
            page = requests.get(url, stream=True)  
            soup = self.make_soup_object(page)
            
            intro_element = soup.find(class_="intro")
            
            if intro_element is not None:
                threadNumber = intro_element.get("id")
                self.make_thread_directory(threadNumber)
                
            else:
                self.puller.next_url()
                continue

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
