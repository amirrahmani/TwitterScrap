from TwitterAPI import TwitterAPI
from twilio.rest import TwilioRestClient
from pync import Notifier
import os
# Desktop notification function
def notify(title, subtitle, link):
    t = '-title {!r}'.format(title)
    s = '-message {!r}'.format(subtitle)
    l = '-open {!r}'.format(link)
    so = '-sound "default"'
    os.system('terminal-notifier {}'.format(' '.join([t, s, l ,so])))

# account info for text message
accountSID = 'YOUR accountSID'
authToken = 'YOUR authToken'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = 'YOUR TwilioNumber'
myCellPhone = 'YOUR Cell Phone number'

# authenticate twitter
API_KEY='YOUR API KEY' #25 alphanumeric characters
API_SECRET='YOUR API_SECRET' #50 alphanumeric characters
ACCESS_TOKEN = 'YOUR ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUT ACCESS_TOKEN_SECRET'
api = TwitterAPI(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

user_id = 2899773086 # every3minutes
#usr_id = 25073877 # realdonaldtrump
#usr_id = 818910970567344128 # vp
#usr_id = 822215679726100480 # potus
r = api.request('statuses/filter', {'follow':str(usr_id)}).get_iterator()
for item in r:
      if item['user']['id']==usr_id:
            print(item['text'])
            print ' '
            notify(title    = "New Tweet",
                  subtitle = item['text'],
                  link     = "New Tweet")
#            twilioCli.messages.create(to=myCellPhone, from_=myTwilioNumber,
#                  body="New Tweet: "+item['text'] )

