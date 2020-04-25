import tweepy
from datetime import timedelta, datetime
from secrets import CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

RANGE = timedelta(days=30)

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    my_tweets = api.user_timeline(count=200)
    for tweet in my_tweets:
        time_since_post = datetime.now() - tweet.created_at
        if time_since_post > RANGE:
            print(time_since_post, tweet.id)
            api.destroy_status(tweet.id)
