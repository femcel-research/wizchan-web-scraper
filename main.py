import os
from utils import Process

list_path = os.path.abspath("./data/lists/urls.txt")
process = Process(list_path)
process.process_current_list()
print("processed")