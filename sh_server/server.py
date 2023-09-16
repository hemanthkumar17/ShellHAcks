from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

from firebase import firebase
fb = firebase.FirebaseApplication('https://dynamo-1697a-default-rtdb.firebaseio.com/', None)

from utils.evaluation import get_groups
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello world!'

username = "Hemanth"

@app.route('/topic', methods =["GET","POST"])
def get_topic():
    # get the topic from the user
    # use this topic to generate the set of questions  
    try:
        data =  request.get_json()
        sub = get_groups(data.topic)
        fb.post(username + "/" + data.topic, {x: p for x, p in enumerate(sub)}, merge=True)

        print("data recieved from client"+data)
        return jsonify({"message":"topic recieved"})
    except Exception as e:
        return jsonify({'error':str(e)}), 400

# get the set of questions
@app.route('/questions', methods=["GET"])
def send_questions():
    data = fb.get(username, '')
    for topic in data:
        subtopics = data[topic].values()
        # print(topic)
    print(subtopics)
    print("get")
    # send the questions to client 
    return ""

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