import twitter
from pprint import pprint
from settings import *
from slack import *
import time

api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                  consumer_secret=TWITTER_CONSUMER_SECRET,
                  access_token_key=TWITTER_ACCESS_TOKEN_KEY,
                  access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

for screenName, slackName in TWITTER_SCREEN_NAMES.items():

    statuses = api.GetUserTimeline(screen_name=screenName)

    currentTime = time.time() + time.altzone

    pprint(time.asctime(time.localtime(currentTime)))

    for status in statuses:
        
        #super hack to remove the time zone on the assumption twitters created at will
        #always be time zone neutral
        createdAt = str(status.created_at).replace("+0000", "")
        createdAtSeconds = time.mktime(time.strptime(createdAt, "%c"))
        timeDiffSeconds = currentTime - createdAtSeconds

        if timeDiffSeconds <= REFRESH_TIME_SECONDS:  
            if status.text.find(SHARE_HASH) != -1:
                slack = Slack()
                slack.token(SLACK_TOKEN)
                slack.channel(SLACK_CHANNEL)  
                slack.text(status.text.replace(SHARE_HASH, ""))
                slack.icon(status.user.profile_image_url)
                slack.userName(slackName)

                if status.media:
                    slack.unfurlMedia(False)
                    for media in status.media:
                        slack.image(media.media_url)
                else:
                    slack.unfurlMedia(True)

                response = slack.postMessage()
                pprint(response.content)     
        else:
            break