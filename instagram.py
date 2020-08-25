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
users = ['robinsharma','joshua_becker','iamjoelbrown','michaelhyatt','elephantjournal','melrobbinslive','alexikonn','mj.demarco','garyvee','tombilyeu','steven','motivation_mondays','nowfuture','6amsuccess','24hoursuccess','motivationmafia','the.success.club','addicted2success','shredded_life','millionaire_mentor','secrets2success','AmbitionCircle','MindsetofGreatness','Before5AM','LuxQuotes','TheFitnessGirlsGuide','SuccessBlueprint','WordsofSuccess','Millionaire.Dream']

dont_like_these = ['naked','nsfw','boob','bath','girls','adult','cuckold','hentai','chaturbate','hotties','sexxxx','pornsex','localgirls','pornlive','nsfwvideo','instablowjob','instansfw','instaadult']
# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)
session.login()
for i in range(12):
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
    users_in_use = random.sample(users, 10)
    set_user_interact(amount = 5, percentage = 50, randomize = True)
    set_comments(comments)
    set_do_follow(True, percentage = 50, times = 1)
    set_do_comment(True, percentage = 50)
    session.set_dont_like(dont_like_these)
    
    
    # let's do this :>
    session.unfollow_users(amount=50, allFollowing=True,
                                       style="LIFO", unfollow_after=3*60*60, sleep_delay=450)
    session.like_by_tags(hashtags_in_use, amount=4, skip_top_posts= True, use_smart_hashtags = True, interact = True, randomize = True)
    follow_likers(users_in_use, photos_grab_amount = 1, follow_likers_per_photo = 2, randomize = True, interact = True)
