from htmldate import find_date
import json
import requests
import os

class MetaCollector:
    def __init__(self, URL, pageName):
        self.URL = URL
        self.pageName = pageName

    def dateToJSON(self):
        folder_path = './web-scraper/data/meta'
        file_name = "thread_" + self.pageName + ".json"
        file_path = os.path.join(folder_path, file_name) 

        url = self.URL
        response = requests.get(url)
        publish_Date = find_date(response.content, extensive_search=True, original_date= True)
        dates = {
            "date published": publish_Date
            }
        
        with open(file_path, "w",  encoding='utf-8') as f:
            json.dump(dates, f)
        

