from htmldate import find_date
from bs4 import BeautifulSoup
import json
import requests
import datetime
import os
import re


# add automatic html, meta, thread folders
class MetaCollector:
    """Collects metadata from a website and stores it in a JSON file"""

    def __init__(self, page, soup, folder_path):
        # Website info
        self.page = page
        self.soup = soup
        self.pageName = soup.find(class_="intro").get("id")

        # File path
        self.folder_path = folder_path
        self.file_name = "meta_" + self.pageName + ".json"
        self.file_path = os.path.join(self.folder_path, self.file_name)

    def date_to_JSON(self):
        """Captures date published, date updated, and date scraped from a specified website"""

        # Uses htmldate lib to find original and update dates
        publish_Date = find_date(
            self.page.content,
            extensive_search=True,
            original_date=True,
            outputformat="%Y-%m-%d %H:%M:%S",
        )
        update_Date = find_date(
            self.page.content,
            extensive_search=False,
            original_date=False,
            outputformat="%Y-%m-%d %H:%M:%S",
        )

        # Assumption is that each time this func is run during scrape, it will capture the time of scrape
        scrape_date = datetime.datetime.now()
        formatted_date = scrape_date.strftime("%Y-%m-%d %H:%M:%S")

        dates = {
            "date_published": publish_Date,
            "date_updated": update_Date,
            "date_scraped": formatted_date,
        }

        return dates

    def page_info_to_JSON(self):
        """Captures page URL, title, description, keywords, site info"""

        # page = requests.get(self.URL, stream=True)
        page = self.page
        # soup = BeautifulSoup(page.content, "html.parser")
        
        # Splits board and thread title
        page_title = self.soup.title.string
        board_and_title = re.split('[-]',page_title)
        for x in range(len(board_and_title)):
            board_and_title[x] = board_and_title[x].strip()
        board = board_and_title[0]
        title = board_and_title[1]

        info = {
            "URL": page.url,
            "board": board,
            "thread_title":title,# for cc its safe to assume each title will be the board name
            "thread_number": self.soup.find(class_="intro").get("id"),
        }
        return info

    def meta_dump(self):
        """Dumps website metadata into a JSON file"""
        metadata = {**self.page_info_to_JSON(), **self.date_to_JSON()}

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
