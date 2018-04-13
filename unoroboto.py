
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
import random
 
#argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'ZfqIBFxE6tESUr3R72rJpMpR6'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '7bINmtOsrsofCY7dNsGLeHObJLjayDxTybymbc1tlEgVJganxD'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '982094157366751234-NV7tEbkISusv7bHhNinOBzTEvpj2eGq'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'KfpFH19YnI0FVUYNlwdVR6JmYNO5QiWl1KACMDQNzaRQn'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

'''
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
'''

num_words = 466543

while(1==1):

	myself = api.search_users("unoroboto")
	for me in myself:
		print 'user = ', 'id = ', me.id, me.screen_name, 'sc = ', me.statuses_count

	my_retweets = api.user_timeline("unoroboto", count=100)
	my_retweet_ids = []
	for tweet in my_retweets:
		my_retweet_ids.append(tweet.entities['user_mentions'][0]['id'])
		print 'tweet = ', tweet.entities['user_mentions'][0]['id']
		print ''

	#print 'my_retweet_ids = ', my_retweet_ids

	num_to_tweet = 1
	num_retweeted = 0

	while num_retweeted < num_to_tweet:

		rand_num = random.randint(1,num_words)
		print 'rand_num = ', rand_num

		#f = open(words.txt., 'r')
		with open('words.txt', 'r') as f:
			for i in range(rand_num):
				f.next()
			for line in f:
				search_string = line
				break			
		f.close

		print 'search_string = ', search_string

		for j in range(1,52):
			users = api.search_users(search_string, per_page=1, page=j)
			for user in users:
				if user.statuses_count == 1 and user.followers_count < 1000:
					print 'user = ', user.id, 'j =', j,  'id = ', user.screen_name, 'sc = ', user.statuses_count
					try:
						print 'lang = ', user.status.lang, 'text = ', user.status.text
						if user.status.lang == 'en' and user.status.id not in my_retweet_ids:
							print 'retweet this!', user.status.text
							api.retweet(user.status.id)
							time.sleep(1800)
							num_retweeted = num_retweeted + 1
							break
					except:
						pass
					print ''

				if num_retweeted >= num_to_tweet:
					break

			if num_retweeted >= num_to_tweet:
				break
