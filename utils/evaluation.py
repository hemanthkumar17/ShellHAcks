from typing import List
import openai
from openai import ChatCompletion
from api_keys import OPENAPI_KEY

# import torch
import json
# from sentence_transformers import util


openai.api_key = OPENAPI_KEY
def get_questions(subtopics: List[List]):
    questions = {"questions": []}
    for topic in subtopics:
        prompt = """
        Follow my instructions precisely. Everytime you receive an input list in the format:
        [
        "Introduction to Programming",
        "Programming languages and paradigms",
        "Setting up the development environment",
        ]
        Write 3 questions to test the understanding of a student who has learned these. Give the output in the format:
        {"questions":
        [
            {"question": "What is programming?", "answer": "Programming is the process of writing instructions for a computer to execute."},
            {"question": "What are programming languages?", "answer": "Programming languages are formal languages used to communicate instructions to a computer."},
            {"question": "Why is setting up the development environment important?", "answer": "Setting up the development environment ensures that all necessary software and tools are installed and configured for programming."}
        ]
        }
        """
        while True:
            try:
                results = ChatCompletion.create(model="gpt-3.5-turbo", messages=[
                    {"role": "user", "content": prompt},
                    {"role": "user", "content": str(topic)}
                ])
                questions["questions"]+= json.loads(results["choices"][0]["message"]["content"])["questions"]
            except:
                continue
            else:
                break

    return questions

def compare(question, answer, answer_truth):
    res = 0
    for i, j, k in zip(question, answer, answer_truth):
        qe = openai.Embedding.create(input = [i], model="text-embedding-ada-002")['data'][0]['embedding']
        ae = openai.Embedding.create(input = [j], model="text-embedding-ada-002")['data'][0]['embedding']
        ate = openai.Embedding.create(input = [k], model="text-embedding-ada-002")['data'][0]['embedding']
        res += (util.pytorch_cos_sim(ae, qe) + util.pytorch_cos_sim(ae, ate)) / 2
    res = res.flatten()[0]
    return res >= 0.8 * len(question), res

def evaluate_test(qa_pairs, answer_truth):
    """Evaluates a list(list(questions)) to give a list(list(answers)) and list(list(answer_truth))
    The first dimension defines the different subtopics (weeks in our case), and second dimension being the list of questions
    Args:
        qa_pairs ("questions": List({"question": "answer"})): Questions and answersthat ChatGPT generated
        answer_truth (List(List(String))): Answer Given by the user

    Returns:
        _type_: _description_
    """
    questions = [x["question"] for x in qa_pairs["questions"]]
    answers = [x["answer"] for x in qa_pairs["questions"]]
    res = []
    for i, j, k in zip(questions, answers, answer_truth):
        res.append([compare(i, j, k)])
    return res


def get_course_list_api(topic = "Programming"):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", 
         "content": """Write a concise course plan about an introduction course to \"""" + topic + """}\" for students who are either starting to learn it or have covered a few topics in it. 
         Write a list of all subtopics that will be taught each week. Remove all the course recap, projects, assignments, and quizzes from the course. 
         Take a deep breath and think about this step by step. Now give me a list of sub-topics to include for teaching them. Give the answer in JSON format, {{week: topics}}"""}
    ]
    )
  return response

def get_groups():
    
  groups=[]
  response=get_course_list_api()
  response=response["choices"][0]["message"]["content"]
  response = response.replace("\\", "").replace("\n", "")
  response=json.loads(response)

  for i in response:
     groups.append(response[i])

  return groups

def get_QNA(questions):
    '''This function expects a list of questions, it will generate 10 new questions, the output will be a dict object
    of the format new_questions={"questions":[{"question":"","answer":""},{},{}]}'''
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
    response = openai.ChatCompletion.create(
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
    
    return new_questions
    