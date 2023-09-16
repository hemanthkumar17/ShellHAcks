from typing import List
import openai
from openai import ChatCompletion
from api_keys import OPENAPI_KEY

import json

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