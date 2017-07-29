import uuid
import apiai
import json

class myAPI:
    def __init__(self, jsonData):
        ai = apiai.ApiAI('390bfd55dc8c4a979998b32b8e884c64')
        self.request = ai.text_request()
        self.request.session_id = str(uuid.uuid4())
        self.jsonData = jsonData

    def GetIntent(self,msg):
        self.request.query = msg
        resp = self.request.getresponse()
        data = json.loads(resp.read())
        retResponse = (str(data)+'&#13;&#10;')
#        if 'intent' in resp['entities']:
#            intent = resp['entities']['intent'][0]['value']
#            confidence = resp['entities']['intent'][0]['confidence']
#            if 0:
#                retResponse =  'category: '+intent+'&#13;&#10;'
#                retResponse +=  'condifence:'+str(confidence)+'&#13;&#10;'
#            retResponse +=  self.jsonData[intent]['response']
#        else:
#            retResponse +=  self.jsonData['None']['response']
        return retResponse