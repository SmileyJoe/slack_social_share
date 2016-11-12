import twitter
from pprint import pprint
from settings import *
import requests
from slack import *
from requests.utils import quote

api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                  consumer_secret=TWITTER_CONSUMER_SECRET,
                  access_token_key=TWITTER_ACCESS_TOKEN_KEY,
                  access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

statuses = api.GetUserTimeline(screen_name=TWITTER_SCREEN_NAME)

slack = Slack()
slack.token(SLACK_TOKEN)
slack.channel(SLACK_CHANNEL)
slack.unfurlMedia(False)

for status in statuses:
     if status.text.find(SHARE_HASH) != -1:
        slack.text(status.text.replace(SHARE_HASH, ""))
        slack.icon(status.user.profile_image_url)
        slack.userName(status.user.screen_name)

        for media in status.media:
             slack.image(media.media_url)

        pprint(slack.postMessage())