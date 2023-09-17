from evaluation import get_groups, get_questions, evaluate_test
# x1 = get_groups()
# x2 = get_groups("Quantum Computing")
# print(x1)
# print(x2)
# x3 = get_questions(x1)
# x4 = get_questions(x2)
# print(x3)
# print(x4)

# qa_pairs = {"questions": [{"answer":"Programming is the process of writing instructions for a computer to execute.","question":"What is programming?"},
#                 {"answer":"Programming concepts are fundamental ideas and principles used in programming, such as variables, control structures, and functions.","question":"What are programming concepts?"},
#                 {"answer":"The basic syntax of a programming language refers to the rules and structure that define how code should be written in that language.","question":"What is the basic syntax of a programming language?"},
#                 {"answer":"Variables are used to store and manipulate data in a program, and data types define the type of data that can be stored in a variable, such as integers, strings, or booleans.","question":"What are variables and data types?"},
#                 {"answer":"Operators are symbols used to perform specific operations on data, and expressions are combinations of operators, variables, and constants to produce a value.","question":"What are operators and expressions?"},
#                 {"answer":"Input refers to the data or information provided to a program, while output refers to the result or response produced by a program.","question":"What is input and output in programming?"}
#                 ]*3}
# answers = ["Programming is the process of writing instructions for a computer to execute.",
#             "Programming concepts are fundamental ideas and principles used in programming, such as variables, control structures, and functions.",
#             "The basic syntax of a programming language refers to the rules and structure that define how code should be written in that language.",
#             "Variables are used to store and manipulate data in a program, and data types define the type of data that can be stored in a variable, such as integers, strings, or booleans.",
#             "Operators are symbols used to perform specific operations on data, and expressions are combinations of operators, variables, and constants to produce a value.",
#             "Input refers to the data or information provided to a program, while output refers to the result or response produced by a program."
#             ]*3
# ans = evaluate_test(qa_pairs=qa_pairs, answer_truth=answers)

# print(ans)
username = "Hemanth"

from firebase import firebase
fb = firebase.FirebaseApplication('https://dynamo-1697a-default-rtdb.firebaseio.com/', None)

data = fb.get(username, '')
topic = list(data.keys())[0]
hash = list(data[topic].keys())[0]
weeks = data[topic][hash]
print(weeks)
print(hash)
week_data = [data[topic][hash][week] for week in weeks]
subtopics = [data[topic][hash][week]['topics'] for week in weeks]
print(subtopics)

path = username + "/" + topic + "/" + hash + "/"
print(path)
print(subtopics)
# for topic in data:
#     subtopics = list(data[topic].values())[0]
# res = [bool(ans[i] and ans[i + 1] and ans[i + 2]) for i in range(0, len(ans) - 2, 3)]
# for t, r in res(subtopics):
#     print(fb.post(path + t, res))
# print(subtopics)
# print(res)