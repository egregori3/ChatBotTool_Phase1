# https://stackoverflow.com/questions/37345215/retrieve-text-from-textarea-in-flask

import os
import json
import myWit
import myLUIS
import myAPI
import convAPI
import mySession
from flask import Flask, request, send_from_directory

# NLU testing page
NLUhtmlHeader = '<center><h1>Eric Gregori OMSCS Advisor NLU Testing - egregori3@gatech.edu<br>Ask me about OMSCS admissions or curriculum</h1></center><br>'
NLUformTest = '<center><form action="nlusubmit" id="textform" method="post"><textarea name="text" cols="40"></textarea><input type="submit" value="Submit"></form></center>'
NLUhtmlWitRespStart = '<h2>Wit.ai response<br><textarea cols="40" rows="10">'
NLUhtmlWitRespEnd   = '</textarea>'
NLUhtmlLUISRespStart = '<h2>LUIS response<br><textarea cols="40" rows="10">'
NLUhtmlLUISRespEnd   = '</textarea>'
NLUhtmlAPIRespStart = '<h2>API.ai response<br><textarea cols="40" rows="10">'
NLUhtmlAPIRespEnd   = '</textarea>'
testForm = NLUhtmlHeader+NLUformTest

# Conversation page
CONVhtmlHeader = '<center><h1>Eric Gregori OMSCS Advisor Conversational Agent - egregori3@gatech.edu</h1><h2>Ask about OMSCS admissions or curriculum.</h2></center>'
CONVformTest = '<center><form action="convsubmit" id="textform" method="post"><textarea name="text" cols="40" placeholder="Enter text and click Submit"></textarea><input type="submit" value="Submit"></form></center>'
CONVhtmlAPIRespStart = '<center><br><textarea cols="80" rows="40" readonly>'
CONVhtmlAPIRespEnd   = '</textarea></center>'
convForm = CONVhtmlHeader+CONVformTest

# Start Flask server - This code runs once when server is started
my_dir = os.path.dirname(__file__)
my_file_path = os.path.join(my_dir, 'OMSCSLexJson1.json')
with open(my_file_path) as json_data:
    OMSCSDict = json.load(json_data)

Session = mySession.mySession()

app = Flask(__name__)

@app.route('/')
def main_page():
    return send_from_directory(my_dir, 'index.html')

#Conversation Testing
@app.route('/conversation')
def ConvPage():
    if Session.Timeout():
        Session.StartSession()
        return convForm
    return ('Sorry, only one session is supported and someone else has it. Try again in:'+str(Session.TimeRemaining())+' seconds')

@app.route('/convsubmit', methods=['POST'])
def csubmit_post():
    if Session.stateDone():
        Session.StartSession()
    if Session.Timeout():
        return 'Your session has timed out. Goto egregori3.pythonanywhere.com to re-enter '
    client = convAPI.convAPI()
    if Session.inValidSession():
        return 'Goto egregori3.pythonanywhere.com'
    APIresp, retState = client.GetIntent(request.form["text"], Session.GetSessionId())
    if retState: Session.ChangeState(retState)
    retResponse =  convForm
    retResponse += CONVhtmlAPIRespStart
    retResponse += ('Session Time remaining:'+str(Session.TimeRemaining())+' seconds&#13;&#10;')
    retResponse += Session.AddResponse(APIresp)
    retResponse += CONVhtmlAPIRespEnd
    return retResponse

#NLU Testing
@app.route('/nlu')
def NLUPage():
    return testForm

@app.route('/nlusubmit', methods=['POST'])
def submit_post():
    WitClient = myWit.myWit( OMSCSDict )
    LUISClient = myLUIS.myLUIS( OMSCSDict )
    APIClient = myAPI.myAPI( OMSCSDict )
    WITresp = WitClient.GetIntent(request.form["text"])
    LUISresp = LUISClient.GetIntent(request.form["text"])
    APIresp = APIClient.GetIntent(request.form["text"])
    retResponse = testForm + '<table style="width:100%" align="center"><tr>'
    retResponse += ('<td>' + NLUhtmlWitRespStart + WITresp + NLUhtmlWitRespEnd + '</td>')
    retResponse += ('<td>' + NLUhtmlLUISRespStart + LUISresp +  NLUhtmlLUISRespEnd + '</td>')
    retResponse += ('<td>' + NLUhtmlAPIRespStart + APIresp +  NLUhtmlAPIRespEnd + '</td>')
    retResponse += '</tr></table>'
    return retResponse

if __name__ == '__main__':
    app.run()