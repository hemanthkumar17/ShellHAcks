from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/topic')
def get_topic():
    # get the topic from the user
    # use this topic to generate the set of questions  
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

