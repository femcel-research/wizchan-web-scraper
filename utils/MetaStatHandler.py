import json
import os


class MetaStatHandler:
    """WIP! Sketching out a class that could be used for collecting statistics in logs and meta files"""

    def __init__(self, thread_meta):
        """Initializes with thread meta stats"""
        # Thread Meta; TODO: Implement getters and such (mostly pseudocode right now)
        if os.path.exists(thread_meta):
            with open(thread_meta) as json_file:
                self.data = json.load(json_file)

            self.dist_post_ids = self.data["dist_post_ids"]  # []; all distinctive post_ids across all scans
            self.lost_post_ids = self.data["lost_post_ids"]  # []; everytime a post is in dist_post_ids but not all_post_ids && not in lost_post_ids already, add here
            self.num_dist_posts = self.data["num_dist_posts"] # += w/ num_new_posts
            self.num_total_posts = self.data["num_total_posts"]  # Posts across all scans; += w/ num_all_posts    
            self.num_lost_posts = self.data["num_lost_posts"] 
        
        else: 
            self.dist_post_ids = []  # []; all distinctive post_ids across all scans
            self.lost_post_ids = []  # []; everytime a post is in dist_post_ids but not all_post_ids && not in lost_post_ids already, add here
            self.num_dist_posts = 0 # += w/ num_new_posts
            self.num_total_posts = 0  # Posts across all scans; += w/ num_all_posts    
            self.num_lost_posts = 0 
           

    def set_scan_values(self, soup):
        self.all_post_ids = []
        original_post = soup.find(class_="post op")
        self.all_post_ids.append(original_post.find(class_="intro").get("id"))

        for reply in soup.find_all(class_="post reply"):
            self.all_post_ids.append(reply.find(class_="intro").get("id"))
        
        self.new_post_ids = []  # post_ids that are in this scan, but not dist_post_ids (though they'll be added l8r)
        self.new_lost_posts = []
        self.num_new_lost_posts = 0
        
        for post_id in self.all_post_ids:
            if post_id not in self.dist_post_ids:
                self.new_post_ids.append(post_id)
        
        for post_id in self.dist_post_ids:
            if post_id not in self.all_post_ids:
                self.new_lost_posts.append(post_id)
                self.num_new_lost_posts += 1

        self.num_all_posts = len(self.all_post_ids)
        self.num_new_posts = len(self.new_post_ids)
    
    def set_thread_values(self):
        """Call after set_scan_values()"""
        
        for post_id in self.new_post_ids:
            if post_id not in self.dist_post_ids:
                self.dist_post_ids.append(post_id)
        for post_id in self.new_lost_posts:
            if post_id not in self.lost_post_ids:
                self.lost_post_ids.append(post_id)
        self.num_dist_posts += self.num_new_posts
        self.num_total_posts += self.num_all_posts
        self.num_lost_posts += self.num_new_lost_posts
    
    def set_site_values(self, site_meta):
        self.num_sitewide_threads = site_meta.get_num_sitewide_threads()  # Maybe won't happen here, but this should be updated with each new thread folder
        self.num_sitewide_total_posts = site_meta.get_num_sitewide_total_posts()  # To += w/ num_all_posts
        self.num_sitewide_dist_posts = site_meta.get_num_sitewide_dist_posts()  # To += w/ num_new_posts
        return

    def get_thread_meta(self):
        return {
            "dist_post_ids" : self.dist_post_ids,
            "lost_post_ids" : self.lost_post_ids,
            "num_dist_posts" : self.num_dist_posts,
            "num_total_posts" : self.num_total_posts,
            "num_lost_posts" : self.num_lost_posts
        }
    
    def get_scan_meta(self):
        return {
            "all_post_ids" : self.all_post_ids,
            "new_post_ids" : self.new_post_ids,
            "new_lost_posts" : self.new_lost_posts,
            "num_all_posts" : self.num_all_posts,
            "num_new_posts" : self.num_new_posts,
            "num_new_lost_posts" : self.num_new_lost_posts
        }
    
    def get_site_meta(self):
        return