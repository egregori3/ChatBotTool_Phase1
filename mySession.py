import uuid

class mySession:
    def __init__(self):
        self.session_id = None
        self.response = ""
        self.state = 'init'

    def StartSession(self):
        self.response = ""
        self.state = 'init'
        self.session_id = str(uuid.uuid4())

    def inValidSession(self):
        return (self.session_id == None)

    def GetSessionId(self):
        return self.session_id

    def AddResponse(self,response):
        self.response = (response + '&#13;&#10;&#13;&#10;' + self.response)
        return self.response

    def ChangeState(self,newState):
        self.state = newState

    def stateDone(self):
        return (self.state == 'done')
