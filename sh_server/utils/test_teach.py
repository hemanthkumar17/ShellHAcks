from teach import get_vids, get_qna

print(get_vids(["Shor's Algorithm", "Grover's Algorithm"]))
qs = ["What is the purpose of an Integrated Development Environment (IDE) in the context of programming?",
               "Can you explain the concept of 'variables' in programming and provide an example of declaring and initializing a variable?",
               "What is the difference between a high-level programming language and a low-level programming language? Give examples of each.",
    ]
print(get_qna(qs))
