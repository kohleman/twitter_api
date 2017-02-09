import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


ckey = '25WRywkcb82VBzfbPDtY4U12G'
csecrect = 'ansUEnDDQ8Etd3tR6UcrK47XcGw6VvKRgEEDBPEA8MB1Om4R8g'
atoken = '829452349294776321-vD9SC53y8Htui3tmHvc0zSNdsKQLKEv'
asecret = 'HsSjs3DRElOOm9ExawAq9O9CKxn2Ml1UHk0gsrcodeaiA'


class listener(StreamListener):

    def on_data(self, raw_data):
        print(raw_data)
        return True

    def on_error(self, status_code):
        print(status_code)



auth = OAuthHandler(ckey, csecrect)
auth.set_access_token(atoken, asecret)
twitterStream = Stream (auth, listener())
twitterStream.filter(track=["trump"])

# api = tweepy.API(auth)
# new_tweets = api.user_timeline(screen_name = "rogerfederer",count=200)
# new_tweets = api.user_timeline(screen_name = "realDonaldTrump",count=10)
#
# outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in new_tweets]
#
# print("Got {0} tweets".format(len(outtweets)))

# for ts in outtweets:
#     print (ts[1])



