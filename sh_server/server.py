from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'


# get the topic
# get the set of questions
# sending the answer back
# eval report
