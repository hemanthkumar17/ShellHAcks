import json
import requests
import openai
import api_keys
openai.api_key = api_keys.API_KEY
def get_course_list_api():
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Write a concise course plan about an introduction course to \"Programming\" for students who are either starting to learn it or have covered a few topics in it. Write a list of all subtopics that will be taught each week. Remove all the course recap, projects, assignments, and quizzes from the course. Take a deep breath and think about this step by step. Now give me a list of sub-topics to include for teaching them. Give the answer in JSON format, {{week: topics}}"}
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