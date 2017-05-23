#-*- coding: utf-8 -*-
from tweepy import StreamListener
from tweepy import Stream
import json
import tweepy
import sys
import jsonpickle
import datetime

#
consumer_key = 'TcSyTjO8ycNRXWUIxxP0rbBFG'
consumer_secret = 'm6uNwnPkMwJkMqWwB4DPqRNlpmfdnEHyJcgiQUsI0tYjpiHaBi'
access_token = '142620900-cOv68WHjBU6WPxPRTGVcxbIaICeSweNGnsxgDNXR'
access_secret = 'QBrzkiCDx8auR5CtjcB8KYdsqnwUXrDFB5LGi51pjgpRQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print ("Problem connecting to API")
    sys.exit(-1)

#start
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
fName = 'stream_tweets' + timestamp  +'.json'
file = open(fName, mode='a', encoding="utf-8")


class CustomStreamListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

    def on_status(self, status):
        print(status)

    def on_data(self, data):
        parsed = json.loads(data)
        text = parsed['text'].translate(non_bmp_map)
        print(text)
        file.write(text)
        return True

    def on_error(self, status):
        print(status)

        return True

    def on_timeout(self):
        print (sys.stderr, 'Timeout...')
        return True

stream = Stream(auth, CustomStreamListener())
stream.filter(track=[u'문재인', u'심상정', u'안철수'])
