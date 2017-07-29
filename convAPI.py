import uuid
import apiai
import json

class convAPI:
    def __init__(self, jsonData):
        ai = apiai.ApiAI('390bfd55dc8c4a979998b32b8e884c64')
        self.request = ai.text_request()
        self.request.session_id = str(uuid.uuid4())
        self.jsonData = jsonData

    def GetIntent(self,msg):
        self.request.query = msg
        resp = self.request.getresponse()
        data = json.loads(resp.read())
        result = data['result']
        sessionID = data['sessionId']
        metadata = result['metadata']
        intent = metadata['intentName']
        confidence = result['score']
        response = result['fulfillment']['speech']
        found = (intent != 'Default Fallback Intent')
        retResponse = 'sessionID:'+str(sessionID)+'&#13;&#10;'
        retResponse += 'intent:'+intent+'&#13;&#10;'
        retResponse += 'confidence:'+str(confidence)+'&#13;&#10;'
        retResponse += ('&#13;&#10;' + response)
        return retResponse, found