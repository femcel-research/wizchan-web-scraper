import os
from utils import Process

# TODO from 10/25 meeting:
# start looking at homepage for links and regularly scrape
# add more structure to add snapshots of when we grab or if things have changed
# look at diff of file or if date updated post dates scraped to see if changes
# more post density on mainpage
# because imageboard
# cross check between catalog page
# double check how date updated is calculated in htmldate
# see if its updated based on post added or if based on post deleted or both
# leave submodule alone until we have canonnical same main
# conflicts due to adding and commiting differences in submodule
# if i run this code with this flag turned on, store data in a file that is untracked by git (testing)
# argparse- parse commandline args;
# ./ main.py -t if you run this package and see -t, run in testing mode
# have a make file that cleans environment? 
# when you make commits you can make commits for specifiic files, be selective of what you add and commit, so changes you are sending are exactly what you want to send
# when you work on different files, look at relationships in different files; if theres a change in a specific file, have a formal specification 
# API COMP127 reference- have a contract on what each funct should do/return
# can put changes in shared slack
# consider commit messages :(
# specify differences in params in git commits
# always pull commits before working
# hash does not change unless submodule change; get back in sync
# when does the submodule in my workflow change, capture in testing file
# if theres little updates to JSON formatting or directory, don't commit those changes to data submodule until you got everything figured out, then you can rescrape
# use command-line for git
# root problem is doing all -> only commit specific files


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
