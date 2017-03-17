from flask import Flask, request
from twilio import twiml
import database
 
app = Flask(__name__)
 
 
@app.route('/sms', methods=['GET', 'POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    resp = twiml.Response()
    ans = database.query(message_body.strip())
    #m=[message_body.strip()]
    #print(m)
    m=[]
    for phoneNo,title,fullName,lastName,profession,keyword in ans:
        name = '{} {} {}'.format(title,fullName,lastName)
        m = m+ ["Name: {}, Profession: {}, Phone Number: {}".format(name, profession,int(phoneNo))]
    if len(m)==0:
       resp.message('No matches.')
    else:
       m = '\n'.join(m)
       resp.message('Found matches: {}'.format(m))
    return str(resp)
if __name__ == '__main__':
    app.run()


