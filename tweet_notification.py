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
accountSID = 'AC00aec6d1f37eab426f064da2b915b146'
authToken = '3ec9cec420a117d374949b65fa06544f'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+16012024175'
myCellPhone = '+16628019241'

# authenticate twitter
API_KEY='0QXnDxqXw9S2dsVpSTumYAgwA' #25 alphanumeric characters
API_SECRET='AJmWZk0qS70LzOediTMsz3Ky2THDJTkjZfKj9Asf5znySqSQ53' #50 alphanumeric characters
ACCESS_TOKEN = '1510941108-MdxwpWheudi9ptPNjkOcdb0I9nuNgFvsTreGeSn'
ACCESS_TOKEN_SECRET = 'lexqzMsBAiWpOUX0MpAI2aQbYNrjs4DajhMrrwnAPOpj1'
api = TwitterAPI(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


usr_id = 25073877 # realdonaldtrump
usr_id = 818910970567344128 # vp
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

