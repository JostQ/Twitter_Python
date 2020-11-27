import tweepy
import os
from settings import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweetId = input("ID du tweet :")

tweet = api.get_status(tweetId, tweet_mode="extended")

nb_retweets = tweet.retweet_count 

rt_nb_file = f"Ressources/retweet_numbers/retweet_number_{tweetId}.txt"
if os.path.exists(rt_nb_file) : 
    f_rt_nb_file = open(rt_nb_file, "r")
    retweet_number = nb_retweets - int(f_rt_nb_file.readlines()[0])
    f_rt_nb_file.close()
else :
    retweet_number = nb_retweets 

f_rt_nb_file = open(rt_nb_file, "w")
f_rt_nb_file.write(str(nb_retweets))
f_rt_nb_file.close()

retweets_list = api.retweets(tweetId, retweet_number)

f = open(f"Ressources/tweets/tweet_{tweetId}.txt", "a")
for retweet in retweets_list :
    if retweet_number != 0 :
        f.write("\n")
        f.write(f"@{retweet.user.screen_name}")
f.close()