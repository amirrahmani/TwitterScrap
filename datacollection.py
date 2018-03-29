# To collect tweets and save them as txt file
from twython import Twython
import sys
import time
import json
from math import ceil

sys.argv = ['','realdonaldtrump'] # by removing this you can pass twitter
                                  # username at command line

handle = sys.argv[1] #takes target twitter screenname as command-line argument
today = time.strftime("%Y%m%d") # today date
txtfilepath = handle + '_' + today + '.txt' # txt filename
jsonfilepath = handle + '_' + today + '.p' # json filename
 
################# Authenticate ####################################################
APP_KEY= #25 alphanumeric characters
APP_SECRET= #50 alphanumeric characters
twitter=Twython(APP_KEY,APP_SECRET,oauth_version=2) #simple authentication object
ACCESS_TOKEN=twitter.obtain_access_token()
twitter=Twython(APP_KEY,access_token=ACCESS_TOKEN)
 
# Adapted from http://www.craigaddyman.com/mining-all-tweets-with-python/
user_timeline = twitter.get_user_timeline(screen_name=handle,count=1) # get most recent tweet
lis = user_timeline[0]['id']-1 #tweet id # for most recent tweet

# Query as deep as necessary
tweetsum= user_timeline[0]['user']['statuses_count'] # Total number of tweets
if tweetsum <200 :  #API only allows depth of 3200 so no point trying deeper than 200*16
      cycles = 1
else:
      cycles=int(ceil(tweetsum / 200))

if cycles>16:
      cycles=16

for i in range(cycles): # iterate through each cycle and read 200 tweets each time
      incremental = twitter.get_user_timeline(screen_name=handle,
      count=200, include_retweets=True, max_id=lis)
      user_timeline.extend(incremental)
      lis = user_timeline[-1]['id']-1 # update the last tweet id
      if i<cycles-1:
            print 'sleeping'
            time.sleep(75) # 75 second rest between api calls. The API allows 15 calls per 15 minutes

user_timeline = reversed(user_timeline)

tweet = {'date':[],'text':[]}

with open(txtfilepath,'wt') as fid:
      for d in user_timeline:
            tweet['date'].append(d['created_at'])
            tweet['text'].append(d['text'])
            fid.write(d['created_at'])
            fid.write("\n")

with open(jsonfilepath,'w') as fid:
      json.dump(tweet,fid)

