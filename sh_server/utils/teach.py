from youtubesearchpython import *
import json
from openai import ChatCompletion
import openai
from .api_keys import OPENAPI_KEY

openai.api_key = OPENAPI_KEY

def get_vids(topic):
    # print(topic)
    return {x["id"]: x["link"] for x in CustomSearch("What is" + topic[0], searchPreferences=VideoSortOrder.viewCount,  limit=10, ).result()['result']}


def get_qna(questions):
    '''This function expects a list of questions, it will generate 10 new questions, the output will be a dict object
    of the format new_questions=[(question, answer), ...]'''
    # questions=["What is the purpose of an Integrated Development Environment (IDE) in the context of programming?",
    #            "Can you explain the concept of 'variables' in programming and provide an example of declaring and initializing a variable?",
    #            "What is the difference between a high-level programming language and a low-level programming language? Give examples of each.",
    # ]
    
    new_questions={"questions":[]}
    prompt="""Give a total of 10 questions, some of them should be of a level similar to the questions I have provided to you.
           Some questions should be more difficult and some questions should be much harder. Ensure that the questions are relevant and help the 
           reader learn. Be sure to provide the answer to the questions, do not repeat any question.  Give the output in the format: 
           {{"questions":
           [
           {
           "question": "","answer":""
           },
           {
           "question": "","answer":""
           },
           ]
           }}
           I have provided the previous questions below:
            """
    question_prompt=""
    for q in questions:
        question_prompt+='\n'+q
    
    prompt+=question_prompt
    response = ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", 
         "content": prompt
         }
    ]
    )

    response=response["choices"][0]["message"]["content"]
    response = response.replace("\\", "").replace("\n", "")
    response=json.loads(response)
    response=response["questions"]

    for r in response:
        r=json.dumps(r)
        r=json.loads(r)
        new_questions["questions"].append(r)
    
    questions = [x["question"] for x in new_questions["questions"]]
    answers = [x["answer"] for x in new_questions["questions"]]
    return list(zip(questions, answers))
    