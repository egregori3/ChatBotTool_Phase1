import apiai
import json

class convAPI:
#    def __init__(self, jsonData):
#        self.jsonData = jsonData

    def GetIntent(self,msg,sessionID):
        ai = apiai.ApiAI('390bfd55dc8c4a979998b32b8e884c64')
        self.request = ai.text_request()
        self.request.session_id = sessionID
        self.request.query = msg
        resp = self.request.getresponse()
        data = json.loads(resp.read())
        result = data['result']
        sessionID = data['sessionId']
        metadata = result['metadata']
        intent = metadata['intentName']
        confidence = result['score']
        response = result['fulfillment']['speech']
        contexts = result['contexts']
        retState = None
        if contexts: retState = contexts[0]['name']
        userInput = result['resolvedQuery']
        retResponse = 'sessionID:'+str(sessionID)+'&#13;&#10;'
        retResponse += 'userInput:'+userInput+'&#13;&#10;'
        retResponse += 'intent:'+intent+'&#13;&#10;'
        retResponse += 'confidence:'+str(confidence)+'&#13;&#10;'
        retResponse += 'contexts:'+str(contexts)+'&#13;&#10;'
        retResponse += ('&#13;&#10;' + response)
        return retResponse, retState