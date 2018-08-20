# TwitterTools

## Scripts to extract tweets from user defined accounts and counting tweets.

### tweet_notification.py is a simple notifaction tool. On a tweet from the specified account it send text and also show a desktop notification. Sending text requires account on Twilio.

### datacollection.py collect the latest 3200 (twitter limit) tweets from the user specified account and save the dates and tweet texts (optional) in a file.

### datacollection_update.py update the file created by datacollection.py with just the new tweets.

### Tweet_counter.ipynb is a tool to count the tweets. It counts the tweets in each day (all day and morning). Also, count the tweets in each week (start day of week is defined by user). Also, calculate the number of tweets from the equivalant current time in previos weeks to the end of that week. Finally it plots the number of tweets at each time of the week

