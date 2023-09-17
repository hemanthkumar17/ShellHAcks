from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

from firebase import firebase
fb = firebase.FirebaseApplication('https://dynamo-1697a-default-rtdb.firebaseio.com/', None)

from utils.evaluation import get_groups, get_questions, evaluate_test
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

        
        sub = get_groups(data['topic'])
        print(sub)
        try:
            fb.post(username + "/" + data['topic'], {f'week_{x}': {"topics": p , "learnt": "false"} for x, p in enumerate(sub)})
            print("data recieved from client",data)
            return jsonify({"message":"topic recieved"})
        except Exception as e:
            return jsonify({'error':str(e)}),400
    except Exception as e:
        return jsonify({'error':str(e)}), 400

# get the set of questions
@app.route('/questions', methods=["GET"])
def send_questions():
    # send the questions to client
    data = fb.get(username, '')
    for topic in data:
        subtopics = list(data[topic].values())[0]
        # print(topic)
    print(subtopics)
    questions = get_questions(subtopics)
    flatten = lambda x: [item for sublist in x for item in sublist]
    return flatten(questions["questions"])

# sending the answer back
@app.route('/answers', methods=["GET","POST"])
def get_answers():
    # get the answers and do the evals
    try:
        data =  request.get_json()
        print("data recieved from client",data)
        qa_pairs = data.qa_pairs
        answers = data.answers
        evals = evaluate_test(qa_pairs=qa_pairs, answer_truth=answers)
        print(evals)

        data = fb.get(username, '')
        for topic in data:
            subtopics = list(data[topic].values())[0]
        print(subtopics)
        # Return evals
        return jsonify({"message":"topic recieved"})
    except Exception as e:
        return jsonify({'error':str(e)}), 400
    return "f"

# eval report
@app.route("/report")
def send_report():
    # send the generated report back to client
    return "send"