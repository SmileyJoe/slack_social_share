# Description #

Python script to share content from social media sites to a slack channel based on user accounts and hashtags.

# Features #
## Networks ##
- Twitter

# Setup #
## Internal ##
The following will need to be added to the route directoy

- `settings.py` - this will have api keys etc in

## Settings.py ##

The settings file will need to have the following values:

```xml
TWITTER_CONSUMER_KEY=<twitter_consumer_key>
TWITTER_CONSUMER_SECRET=<twitter_consumer_secret>
TWITTER_ACCESS_TOKEN_KEY=<twitter_access_token_key>
TWITTER_ACCESS_TOKEN_SECRET=<twitter_access_token_secret>
#TWITTER_SCREEN_NAMES={"twitter_username":"slack_username","twitter_username_two":"slack_username_two"}
TWITTER_SCREEN_NAMES=<dict_of_twitter_accounts_to_check_and_slack_usernames>

SLACK_TOKEN=<slack_api_token>
SLACK_CHANNEL=<slack_channel_to_share_to>

SHARE_HASH=<hashtag_to_share>

#The interval between scripts running, posts older then this wont be posted
REFRESH_TIME_SECONDS=<seconds_interval>
```

## Dependencies ##

The script relies on [python-twitter](https://github.com/bear/python-twitter), this can be installed through pip:

```
$ pip install python-twitter
```

Please see the instructions in the projects `README` for more information.