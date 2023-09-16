import json
import requests
import openai
import api_keys
openai.api_key = api_keys.API_KEY
# print(openai.Model.list())
response={
  "Week 1": [
    "Introduction to Programming",
    "Programming languages and paradigms",
    "Setting up the development environment",
    "Writing and running simple programs",
    "Basic syntax and variables"
  ],
  "Week 2": [
    "Data types and variables",
    "Arithmetic operations",
    "User input and output",
    "Conditional statements (if, else, elif)",
    "Simple program control flow"
  ],
  "Week 3": [
    "Loops (for, while)",
    "Lists and arrays",
    "Working with strings",
    "Functions and modular programming",
    "Debugging techniques"
  ],
  "Week 4": [
    "Introduction to algorithms",
    "Algorithm design and problem-solving",
    "Recursion",
    "File I/O operations",
    "Error handling and exceptions"
  ],
  "Week 5": [
    "Introduction to object-oriented programming (OOP)",
    "Classes and objects",
    "Inheritance and polymorphism",
    "Encapsulation and abstraction",
    "Introduction to libraries and frameworks"
  ],
  "Week 6": [
    "Version control using Git",
    "Collaborative coding and code sharing",
    "Software development methodologies",
    "Introduction to web development",
    "Overview of databases and SQL"
  ]
}

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
  trial="{\n   \"1\": [\n      \"Introduction to Programming\",\n      \"Benefits of learning to code\",\n      \"Introduction to programming languages\",\n      \"Writing your first program\",\n      \"Executing a program\"\n   ],\n   \"2\": [\n      \"Variables\",\n      \"Data types\",\n      \"Working with strings\",\n      \"Arithmetic operators\",\n      \"Order of operations\"\n   ],\n   \"3\": [\n      \"Conditional statements\",\n      \"Logical operators\",\n      \"Comparison operators\",\n      \"Nested conditionals\",\n      \"Case statements\"\n   ],\n   \"4\": [\n      \"Loops\",\n      \"For loop\",\n      \"While loop\",\n      \"Nested loops\",\n      \"Loop control statements\"\n   ],\n   \"5\": [\n      \"Arrays\",\n      \"Creating and accessing arrays\",\n      \"Array manipulation\",\n      \"Multidimensional arrays\",\n      \"Array iteration\"\n   ],\n   \"6\": [\n      \"Functions\",\n      \"Function definition\",\n      \"Function parameters\",\n      \"Returning values\",\n      \"Scope and local variables\"\n   ],\n   \"7\": [\n      \"Error handling\",\n      \"Understanding and handling exceptions\",\n      \"Try-catch blocks\",\n      \"Throwing custom exceptions\",\n      \"Debugging techniques\"\n   ],\n   \"8\": [\n      \"Introduction to object-oriented programming\",\n      \"Classes and objects\",\n      \"Attributes and methods\",\n      \"Encapsulation\",\n      \"Inheritance\"\n   ],\n   \"9\": [\n      \"File handling\",\n      \"Reading from and writing to files\",\n      \"Working with file streams\",\n      \"Error handling in file operations\",\n      \"File manipulation\"\n   ],\n   \"10\": [\n      \"Introduction to algorithms\",\n      \"Algorithm design principles\",\n      \"Brute force algorithms\",\n      \"Searching and sorting algorithms\",\n      \"Recursion\"\n   ]\n}"
  # print("Write a concise course plan about an introduction course to \"Programming\"for students who are either starting to learn it or have covered a few topics in it. Write a list of all subtopics that will be taught each week. Remove all the course recap, projects, assignments, and quizzes from the course. Take a deep breath and think about this step by step. Now give me a list of sub-topics to include for teaching them. Give the answer in JSON format, {week: topics}")
  response=response["choices"][0]["message"]["content"]
  response = response.replace("\\", "").replace("\n", "")
  response=json.loads(response)

  for i in response:
     groups.append(response[i])

  return groups