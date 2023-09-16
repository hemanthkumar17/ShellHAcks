from flask import Flask
app = Flask(__name__)

from firebase import firebase
fb = firebase.FirebaseApplication('https://dynamo-1697a-default-rtdb.firebaseio.com/', None)

from utils.evaluation import get_groups

@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/topic')
def get_topic():
    # get the topic from the user
    # use this topic to generate the set of questions  
    topic = "Programming"
    username = "Hemanth"
    sub = get_groups(topic)
    fb.post(username + "/" + topic, {x: p for x, p in enumerate(sub)})
    print(fb.get(username + "/", topic))
    return "c"

# get the set of questions
@app.route('/questions')
def send_questions():
    
    # send the questions to client 
    return "a"

# sending the answer back
@app.route('/answers')
def get_answers():
    # get the answers and do the evals
    return "f"

# eval report
@app.route("/report")
def send_report():
    # send the generated report back to client
    return "send"

