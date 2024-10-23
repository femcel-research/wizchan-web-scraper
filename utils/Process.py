import UrlPuller
import os
import requests
from utils import TextSaver


# Input txt file with URLs
puller_file = os.path.join('URLs', 'list.txt')  # Sample txt file
puller = UrlPuller.UrlPuller(puller_file)

# For each URL
for i in range(puller.get_size()):
    url = puller.get_url
    page = requests.get(url, stream=True)  # Gets page from URL
    # HTML file
    # JSON metadata file
    # JSON thread content file
    # Add URL to list of processed URLs
    puller.next_url

# Save list of processed URLs to txt file