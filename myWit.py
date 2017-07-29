from wit import Wit

class myWit:
    def __init__(self, jsonData):
        self.client = Wit(access_token='AAO3SR25HFJLRCBVSX6AOE7DFSNJTDGN')
        self.jsonData = jsonData

    def GetIntent(self,msg):
        resp = self.client.message(msg)
        retResponse = (str(resp)+'&#13;&#10;')
        if 'intent' in resp['entities']:
            intent = resp['entities']['intent'][0]['value']
#            confidence = resp['entities']['intent'][0]['confidence']
#            if 0:
#                retResponse =  'category: '+intent+'&#13;&#10;'
#                retResponse +=  'condifence:'+str(confidence)+'&#13;&#10;'
            retResponse +=  self.jsonData[intent]['response']
        else:
            retResponse +=  self.jsonData['None']['response']
        return retResponse