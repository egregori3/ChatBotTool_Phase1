class myState:
    def __init__(self):
        self.client = None
        self.state = 'initialQuestion'

    def StartSession(self, client):
        self.client = client

    def CheckClient(self):
        return self.client == None

    def GetClient(self):
        return self.client

