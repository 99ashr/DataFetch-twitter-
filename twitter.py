#!/usr/bin/python3

import tweepy

# consumer keys and access tokens, used for OAuth
consumer_key = 'LGye31Hhy2JRtAXNDCDYd6mHp'
consumer_secret = 'zFxgplx19ldxxMeODOK7VPvHeHzcsUJkSTT8x2ymoSPBMzKscE'
access_token = '708596665163366401-uivthHeDy1CcAn190RA5jk6HWUy2JE7'
access_token_secret = 'Pe2OxwMS1NmrFOVEMsqMieB0IkwPVKqUrZXSCG0wHgGfV'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# creation of the actual interface, using authentication
api = tweepy.API(auth)
#api.update_status('Test')


#!!!Get information about yourself!!!

user = api.me()

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))


#!!!Get information about any user!!!

user_name=input("Enter the user you want to search:  ")
user = api.get_user(user_name)

print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))


#!!!Search tweet!!!

tweet=input("Enter whatever you wanna search here:  ")
search = tweepy.Cursor(api.search, q=tweet, lang="en").items(30)

#!!!Printing tweets!!!

for item in search:
    print (item.text)
