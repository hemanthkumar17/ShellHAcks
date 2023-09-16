from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/topic', methods =["GET","POST"])
def get_topic():
    # get the topic from the user
    # use this topic to generate the set of questions  
    try:
        data =  request.get_json();
        print("data recieved from client"+data)
        return jsonify({"message":"topic recieved"})
    except Exception as e:
        return jsonify({'error':str(e)}), 400

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

