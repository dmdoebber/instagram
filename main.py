from instagrapi import Client
from prettytable import PrettyTable
import datetime

cl = Client()

session_id = input('session_id: ')

cl.login_by_sessionid(session_id)

print('[', datetime.datetime.now(), '] fetching following...')
following = cl.user_following(str(cl.user_id))

print('[', datetime.datetime.now(), '] fetching followers...')
followers = cl.user_followers(str(cl.user_id))

following_ids = set(y.pk for _, y in following.items())
followers_ids = set(y.pk for _, y in followers.items())

not_following_me_back = following_ids.difference(followers_ids)
im_not_following_back = followers_ids.difference(following_ids)
mutual_followers = following_ids.intersection(followers_ids)

table_mutual_followers = PrettyTable()
for user_id in mutual_followers:
    profile = followers[user_id]
    table_mutual_followers.add_row([profile.pk, profile.username, profile.full_name])

table_im_not_following_back = PrettyTable()
for user_id in im_not_following_back:
    profile = followers[user_id]
    table_im_not_following_back.add_row([profile.pk, profile.username, profile.full_name])

table_not_following_me_back = PrettyTable()
for user_id in not_following_me_back:
    profile = following[user_id]
    table_not_following_me_back.add_row([profile.pk, profile.username, profile.full_name])


table_header = ['ID', 'Username', 'Nome']

table_mutual_followers.field_names = table_header
table_im_not_following_back.field_names = table_header
table_not_following_me_back.field_names = table_header

print(table_mutual_followers)
print(table_im_not_following_back)
print(table_not_following_me_back)
