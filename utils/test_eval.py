from evaluation import get_groups, get_questions
x1 = get_groups()
x2 = get_groups("Quantum Computing")
print(x1)
print(x2)
x3 = get_questions(x1)
x4 = get_questions(x2)
print(x3)
print(x4)