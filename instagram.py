# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:34:26 2020

@author: joshua clymer
"""

import instagram_private_api as instaAPI
import pprint
import numpy as np
import time

user_name = 'clymerjoshua'
password = 'J0$hu@1Wormgear'

api = instaAPI.Client(user_name, password, auto_patch = True)

pp = pprint.PrettyPrinter(indent=4)

def randWait(avgtime):
    waitFor = np.random.normal(loc = avgtime, scale = avgtime * 0.3)
    if waitFor < 0:
        waitFor = 0
    time.sleep(waitFor)
    return


def likePostsOnFeed():
    next_max_id = ""
    while True:
        if next_max_id == "":
            feed = api.feed_timeline()
        else:
            feed = api.feed_timeline(max_id = next_max_id)
        next_max_id = feed['next_max_id']
        print("requesting another page")
        posts = [item for item in feed.get('feed_items', [])
                 if item.get('media_or_ad')]  
        for post in posts:
            id = post['media_or_ad']['id']
            user_full_name = post['media_or_ad']['user']['username']
            try:
                api.post_like(id, module_name='feed_timeline')
                print('botty boy liked post by {}'.format(user_full_name))
            except Exception as e: 
                print(e)
        randWait(1)
        
#Main


#post_comment(media_id, comment_text)
"""
for media_id in media_ids:
    instaAPI.post_like(media_id, module_name='feed_timeline')
"""

#feed_tag(tag, rank_token, **kwargs) potentially use this function to comment on posts in #selfimprovement