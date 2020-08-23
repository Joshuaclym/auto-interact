# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:07:58 2020

@author: joshu
"""

from instapy import InstaPy
from instapy import smart_run
import random
# login credentials
insta_username = 'duglapp'
insta_password = 'Duglisawesome'

comments = ['Nice! :thumbsup:', 'I love your profile! @{}',
            'Love your posts @{}', 'Getting inspired by you @{}', ':raised_hands: Yes!']
hashtags = ['productivity', 'productivitytips', 'goals', 'mondaymotivation',
            'selfimprovement', 'personaldevelopment', 'reflection', 'habit',
            'goalsetting', 'dailymotivation', 'selfhelp',
            'inspireothers', 'gogetit', 'financialfreedom', 'weighttraining',
            'getfit', 'gymtime', 'youcandoit', 'justdoit', 'motivational',
            'healthyhabits', 'eatinghealthy', 'gains', 'progress', 'grind',
            'diet', 'hustle', 'success', 'wealth', 'workout', 'fitfam',
            'selflove', 'meditation', 'selfcare', 'loveyourself', 'bodypositive',
            'confidence', 'intention', 'intentionalliving']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)
session.login()
while True:
    # settings
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                                 peak_likes_hourly=57,
                                 peak_likes_daily=585,
                                 peak_comments_hourly=21,
                                 peak_comments_daily=182,
                                 peak_follows_hourly=48,
                                 peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4700)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=1.34,
                                    delimit_by_numbers=True,
                                    max_followers=8500,
                                    max_following=4490,
                                    min_followers=100,
                                    min_following=56,
                                    min_posts=10,
                                    max_posts=1000)

    hashtags_in_use = random.sample(hashtags, 10)

    # let's do this :>
    session.like_by_tags(hashtags_in_use, amount=20)
    session.set_dont_like(["naked", "nsfw", "fuck", "shit"])
    session.set_do_follow(True, percentage=50)
    session.set_do_comment(True, percentage=50)

    session.unfollow_users(amount=40, allFollowing=True,
                           style="LIFO", unfollow_after=3*60*60, sleep_delay=450)
