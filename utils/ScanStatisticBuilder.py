class ScanStatisticBuilder:
    """WIP! Sketching out a class that could be used for collecting statistics in logs and meta files"""

    def __init__(self, initial_meta, site_meta):
        # Thread Meta; TODO: Implement getters and such (mostly pseudocode right now)
        self.dist_post_ids = initial_meta.get_dist_post_ids()  # []; all distinctive post_ids across all scans
        self.lost_post_ids = initial_meta.get_lost_post_ids()  # []; everytime a post is in dist_post_ids but not all_post_ids && not in lost_post_ids already, add here
        self.num_dist_posts = initial_meta.get_num_dist_posts() # += w/ num_new_posts
        self.num_total_posts = initial_meta.get_num_total_posts()  # Posts across all scans; += w/ num_all_posts

        # Scan Meta
        self.all_post_ids = []  # All post_ids in current scan
        self.new_post_ids = []  # post_ids that are in this scan, but not dist_post_ids (though they'll be added l8r)
        self.lost_post_ids = []  # post_ids that are in dist_post_ids, but not this scan
        self.num_all_posts = 0
        self.num_new_posts = 0
        self.num_lost_posts = 0

        # Site Meta
        self.num_sitewide_threads = site_meta.get_num_sitewide_threads()  # Maybe won't happen here, but this should be updated with each new thread folder
        self.num_sitewide_total_posts = site_meta.get_num_sitewide_total_posts()  # To += w/ num_all_posts
        self.num_sitewide_dist_posts = site_meta.get_num_sitewide_dist_posts()  # To += w/ num_new_posts
