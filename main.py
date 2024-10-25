import os
from utils import Process

# Please note when making lists of URLs:
# - One URL per line
# - Check the thread number against the thread numbers of URLs in processed 
#   (not the message number! For example, in https://crystal.cafe/feels/res/117906.html#117998,
#   the thread number is 117906, not 117998!)

list_path = os.path.abspath("./data/lists")
file_path = os.path.join(list_path, "urls.txt")
process = Process(file_path)
process.process_current_list()
print("processed")