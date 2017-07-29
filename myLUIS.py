import urllib.request
import urllib.parse
import json


class myLUIS:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.url = 'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/5dd6e368-995f-4c80-ad5c-73307670cf7d?subscription-key=c2cfda8e3e92482d95b275b1ae5e131f&timezoneOffset=0&verbose=true&q='

    def GetIntent(self,msg):
        urlQuestion = urllib.parse.quote(msg)
        webURL = urllib.request.urlopen(self.url+urlQuestion)
        resp = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        data = json.loads(resp.decode(encoding))
        intent = data['topScoringIntent']['intent']
#        confidence = data['topScoringIntent']['score']
        return str(data) +'&#13;&#10;'+ self.jsonData[intent]['response']
