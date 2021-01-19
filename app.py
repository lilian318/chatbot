from cht import Chat,reflections
from flask import Flask, render_template, request
from keywords.KEY import key,Count
from pairs.PAIR import pairs
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__, template_folder='templates')

pairs =[['('+key[i]+')',[pairs[i]]] for i in range(Count)]
@app.route('/', methods=['GET', 'POST'])
def samplefunction():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        greetIn = request.form['human']
        greetOut = c(greetIn)
        return render_template('index.html',bot1=greetOut,bot2 = greetIn)
def c(x):
  chat = Chat(pairs,reflections)
  #print(chat.respond(x))
  return chat.respond(x)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming with a simple text message."""
    resp = MessagingResponse()
    phoneno=request.form.get('From')
    msg=request.form.get('Body')
    chat = Chat(pairs,reflections)
    
    #print(msg)
    resp.message(chat.respond(msg))
    return str(resp)






if __name__ == '__main__':
    app. run(debug=True)


