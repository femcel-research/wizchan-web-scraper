# web-scraper

## How to read different meta values
### thread_meta
**["dist_post_ids"]** is the list of distinctive post_ids accross all scans for a single thread
**["lost_post_ids"]** (untested) is a list of post_ids that are in ["dist_post_ids"], but not a subsequent scan (also needs to not alread be in ["lost_post_ids"] already)
**["num_dist_posts"]** is a count that gets added to using ["num_new_posts"] on every scan
**["num_total_posts"]** is a count that gets added to using ["num_all_posts"] on every scan
**["num_lost_posts"]** is a count of every post that was formerly scanned for the current thread, but was not in a subsequent scan
### scan_meta
**["all_post_ids"]** is a list of all post_ids (including post_ids that were in prior scans) that were scanned
**["new_post_ids"]** is a list of post_ids that were scanned and didn't already exist in ["dist_post_ids"]
**["new_lost_posts"]** (untested) is a list of post_ids that are in ["dist_post_ids"], but not this scan (also needs to not alread be in ["lost_post_ids"] already)
**["num_all_posts"]** is a count of all posts that were scanned
**["num_new_posts"]** is a count of all posts that were scanned and didn't already exist in ["dist_post_ids"]
**["num_new_lost_posts"]** is a count of all posts that are in ["dist_post_ids"], but not this scan (also needs to not alread be in ["lost_post_ids"] already)
### site_meta
(WIP) **["num_sitewide_threads"]** is a count of all threads (Currently a duplicate of ["num_sitewide_total_posts"])
**["num_sitewide_total_posts"]** is a count of all posts across all scans (including duplicates) across all threads
(WIP) **["num_sitewide_dist_posts"]** is a count of all posts across all scans across all threads (only counting 1 per set of duplicates)