from requests.utils import quote
import requests

class Slack:
    __url = "https://slack.com/api/"
    __args = "pretty=1&as_user=false"
    __attachments = ""

    def token(self, token):
        self.addArg("token", token)

    def channel(self, channel):
        self.addArg("channel", channel)

    def unfurlMedia(self, unfurlMedia):
        self.addArg("unfurl_media", str(unfurlMedia))

    def text(self, text):
        self.addArg("text", text)

    def icon(self, iconUrl):
        self.addArg("icon_url", iconUrl)
    
    def userName(self, userName):
        self.addArg("username", userName)

    def image(self, imageUrl):
        if self.__attachments:
            self.__attachments += ","

        self.__attachments += "{'image_url': '%s', 'fallback': 'Image'}" % (imageUrl)

    def postMessage(self):
        if self.__attachments:
            self.addArg("attachments", "[" + self.__attachments + "]")

        url = self.__url + "chat.postMessage?" + self.__args
        response = requests.get(url)
        return response

    def getTweetUrl(self, username, id):
        return "https://twitter.com/%s/status/%s?lang=en" %(username, id)

    def addArg(self, key, value):
        self.__args += "&" + key + "=" + quote(value, safe="")