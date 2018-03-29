# to collect last 3200 tweets of an account and save tweet dates and texts to a file
from twython import Twython
import sys
import time
import simplejson
from math import ceil

sys.argv = ['','realdonaldtrump'] # by removing this you can pass twitter 
                                  # username at command line

parentpathi ='your path'
handle = sys.argv[1] # takes target twitter screenname as command-line argument
today = time.strftime("%Y%m%d")
csvfilepath = parentpath+'/'+handle+'_'+today+'.csv'
txtfilepath = parentpath+'/'+handle+'_'+today+'.txt'
 
#authenticate
APP_KEY = #25 alphanumeric characters
APP_SECRET = #50 alphanumeric characters
twitter=Twython(APP_KEY,APP_SECRET,oauth_version=2) #simple authentication object
ACCESS_TOKEN=twitter.obtain_access_token()
twitter=Twython(APP_KEY,access_token=ACCESS_TOKEN)
 
#adapted from http://www.craigaddyman.com/mining-all-tweets-with-python/
#user_timeline=twitter.get_user_timeline(screen_name=handle,count=200) #if doing 200 or less, just do this one line
user_timeline=twitter.get_user_timeline(screen_name=handle,count=1) #get most recent tweet
lis=user_timeline[0]['id']-1 #tweet id # for most recent tweet
#only query as deep as necessary
tweetsum= user_timeline[0]['user']['statuses_count']
if tweetsum <200 :
      cycles = 1
else:
      cycles=int(ceil(tweetsum / 200))

if cycles>16:
    cycles=16 #API only allows depth of 3200 so no point trying deeper than 200*16
#time.sleep(60)
for i in range(0, cycles): ## iterate through all tweets up to max of 3200
    incremental = twitter.get_user_timeline(screen_name=handle,
    count=200, include_retweets=True, max_id=lis)
    user_timeline.extend(incremental)
    lis=user_timeline[-1]['id']-1
    print 'sleeping'
    time.sleep(75) # 75 second rest between api calls. The API allows 15 calls per 15 minutes
 

with open(txtfilepath,'wt') as fid:
      for d in reversed(user_timeline):
            fid.write(d['created_at'])#+ ' , ' +\
#                      d['text'].encode('ascii','ignore'))
            fid.write("\n")


