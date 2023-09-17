from evaluation import get_groups, get_questions, evaluate_test
# x1 = get_groups()
# x2 = get_groups("Quantum Computing")
# print(x1)
# print(x2)
# x3 = get_questions(x1)
# x4 = get_questions(x2)
# print(x3)
# print(x4)

username = "Hemanth"

from firebase import firebase
fb = firebase.FirebaseApplication('https://dynamo-1697a-default-rtdb.firebaseio.com/', None)

data = fb.get(username, '')
topic = list(data.keys())[0]
hash = list(data[topic].keys())[0]
weeks = data[topic][hash]
week_data = [data[topic][hash][week] for week in weeks]
subtopics = [data[topic][hash][week]['topics'] for week in weeks if not data[topic][hash][week]['learnt']]

path ="/" + topic + "/" + hash + "/"

print(subtopics)