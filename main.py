import twitter
from pprint import pprint
from settings import *
import requests
from requests.utils import quote

api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                  consumer_secret=TWITTER_CONSUMER_SECRET,
                  access_token_key=TWITTER_ACCESS_TOKEN_KEY,
                  access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

statuses = api.GetUserTimeline(screen_name=TWITTER_SCREEN_NAME)
#print([s for s in statuses])

#twitterUrl = "https://twitter.com/%s/status/%s?lang=en"

slackBase = "https://slack.com/api/"
slackChatPost = slackBase + "chat.postMessage?"

slackAttachments = "&attachments=%s"
slackAttachmentsImage = "{'image_url': '%s', 'fallback': 'test fallback'}"
slackToken = "&token=" + SLACK_TOKEN
slackChannel = "&channel=" + quote(SLACK_CHANNEL, safe='')
slackPretty = "&pretty=1"
slackUnfurlMedia = "&unfurl_media=false"

slackUrl = slackChatPost + slackToken + slackChannel + slackPretty + slackUnfurlMedia

for s in statuses:
    if s.text.find(SHARE_HASH) != -1:
        slackText = "&text=" + quote(s.text, safe='')
        slackIcon = "&icon_url=" + quote(s.user.profile_image_url, safe="")
        slackUsername = "&as_user=false&username=" + quote(s.user.screen_name, safe='')

        slackUrl = slackUrl + slackText + slackIcon + slackUsername

        first = True
        images = ""
        for m in s.media:
            if first:
                first = False
            else:
                images = images + ","
            images = images + slackAttachmentsImage % (m.media_url)

        if images:
            slackExtras = slackAttachments % (quote("[" + images + "]", safe=""))
            slackUrl = slackUrl + slackExtras
        
        response = requests.get(slackUrl)
        pprint(response.content)