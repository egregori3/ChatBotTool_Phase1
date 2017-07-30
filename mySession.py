import uuid
import time

class mySession:
    def __init__(self):
        self.session_id = None
        self.response = ""
        self.state = 'init'
        self.SessionTime = 120

    def StartSession(self):
        self.response = ""
        self.state = 'startDialog'
        self.session_id = str(uuid.uuid4())
        self.start_time = time.time()

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

    def elapsedTime(self):
        return time.time() - self.start_time

    def Timeout(self):
        return (self.state == 'init' or self.elapsedTime() > self.SessionTime)

    def TimeRemaining(self):
        return max((self.SessionTime - self.elapsedTime()), 0)
