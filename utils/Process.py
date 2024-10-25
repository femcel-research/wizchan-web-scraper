from bs4 import BeautifulSoup
import HTMLCollector
import MetaCollector
import TextCollector
import UrlPuller
import os
import requests

class Process:
    """Takes in a text file of URLs then loops through them, 'processing' each one"""

    def __init__(self, url_list_file):
        """Pass in the list.txt of URLs you want to be processed"""
        self.puller = UrlPuller.UrlPuller(url_list_file)

    def log_processed_url(url):
        """Save list of processed URLs to txt file in data/processed"""
        with open("./web-scraper/data/processed/processed.txt", "a") as file:
            file.write(url + '\n')

    def make_soup_object(page):
        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    def make_thread_directory(id):
        """Creates a new folder to associate with the thread being processed"""
        thread_folder_path = "./web-scraper/data/" + id
        os.mkdir(thread_folder_path)

    def process_current_list(self):
        """For each URL in the list, get HTML, metadata JSON, and content JSON"""

        for i in range(self.puller.get_size()):
            # Gets page from URL and makes a new directory for the thread
            url = self.puller.get_url
            page = requests.get(url, stream=True)  
            soup = self.make_soup_object(page)
            id = soup.find(class_="intro").get("id")
            self.make_thread_directory(id)

            # HTML file
            html = HTMLCollector(soup)
            html.saveHTML()

            # JSON metadata file
            meta = MetaCollector(page, soup)
            meta.meta_dump()

            # JSON thread content file
            content = TextCollector(soup)
            content.write_thread()

            # Add URL to list of processed URLs
            self.log_processed_url(url)

            self.puller.next_url