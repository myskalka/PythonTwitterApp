import os
import tweepy as tw
import pandas as pd

consumer_key= 'yourkeyhere'
consumer_secret= 'yourkeyhere'
access_token= 'yourkeyhere'
access_token_secret= 'yourkeyhere'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

companyDict = {1: 'IBM', 2: 'Microsoft', 3: 'GE', 4: 'SAP', 5: 'Oracle', 6: 'ExxonMobile', 7: 'HP', 8: 'Accenture', 9: 'FedEx', 10: 'Siemens', 11: 'Cisco', 12: 'J. P. Morgan', 13: 'Intel', 14: 'UBS', 15: 'Boeing', 16: 'John Deere', 17: 'Northrop Gruman', 18: 'Huawei', 19: 'Caterpillar', 20: 'UPS'}

class StreamListener(tw.StreamListener):
    def on_status(self, status):
        print(status.id_str)
    
    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()
        
        
streamlistener = StreamListener()
stream = tw.Stream(auth=api.auth, listener=streamlistener, tweet_mode='extended')

