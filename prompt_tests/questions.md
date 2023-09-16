# To generate Sub-topics given a main topic that the user wants to learn

 - """
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
    [['Introduction to programming', 'Understanding programming languages', 'Setting up development environment', 'Basic concepts: variables, data types, and operators', 'Input and output', 'Control flow: if statements and loops'], ['Functions and methods', 'Working with arrays and lists', 'Working with strings', 'Debugging and error handling', 'Introduction to object-oriented programming'], ['Classes and objects', 'Inheritance and polymorphism', 'File I/O: reading and writing files', 'Exception handling', 'Introduction to data structures: stacks and queues'], ['Recursion', 'Working with dictionaries and sets', 'Modules and libraries', 'Testing and debugging strategies', 'Introduction to algorithms and complexity']]
```
['Introduction to programming', 'Role and importance of programming', 'Basic syntax and structure of a program', 'Data types and variables', 'Input and output', 'Operators and expressions']
{'question': 'What is the role and importance of programming?', 'answer': 'Programming plays a crucial role in various fields, including software development, data analysis, and artificial intelligence.'}
['Conditional statements (if, else if, else)', 'Logical operators', 'Comparison operators', 'Nested conditionals', 'Switch statements']
{'question': 'What are comparison operators?', 'answer': 'Comparison operators are used to compare two values and determine their relationship, such as equality, inequality, or order.'}
['Loops (for, while, do while)', 'Break and continue statements', 'Iterating over lists and arrays', 'Nested loops', 'Common loop patterns']
{'question': 'Why is iterating over lists and arrays important?', 'answer': 'Iterating over lists and arrays allows us to access and process each element within them.'}
['Functions and procedures', 'Function parameters and return values', 'Function overloading', 'Recursion', 'Scope and variable visibility']
{'question': 'What is scope and variable visibility?', 'answer': 'Scope refers to the visibility or accessibility of variables, and variable visibility defines where a variable can be accessed and manipulated in a program.'}
['Arrays and lists', 'Accessing and modifying array elements', 'Multidimensional arrays', 'Common array operations', 'ArrayLists and their usage']
{'question': 'What are multidimensional arrays?', 'answer': 'Multidimensional arrays are arrays that contain other arrays as their elements, forming a grid-like structure.'}
['Strings and string manipulation', 'String concatenation', 'String methods', 'String formatting', 'Regular expressions']
{'question': 'What are string methods?', 'answer': 'String methods are built-in functions that operate on strings to perform various operations, such as extracting substrings or changing case.'}
['Introduction to object-oriented programming', 'Classes and objects', 'Encapsulation', 'Inheritance', 'Polymorphism']
{'question': 'What is polymorphism?', 'answer': 'Polymorphism is the ability of an object to take on many forms. In object-oriented programming, it allows objects of different classes to be treated as objects of a common superclass.'}
['Working with files', 'Reading and writing text files', 'Serialization', 'Working with directories', 'Error handling (exceptions and try-catch)']
{'question': 'What is serialization?', 'answer': 'Serialization is the process of converting an object into a format that can be easily stored, transmitted, or reconstructed later.'}
['Introduction to debugging', 'Common debugging techniques', 'Using a debugger tool', 'Debugging strategies', 'Best practices for debugging']
{'question': 'Why is using a debugger tool helpful in the debugging process?', 'answer': 'Using a debugger tool allows for more efficient and precise debugging by providing features like breakpoints, variable inspection, and stepping through the code.'}
['Introduction to algorithms', 'Algorithm design and analysis', 'Searching and sorting algorithms', 'Recursion in algorithms', 'Time and space complexity']
{'question': 'What are searching and sorting algorithms?', 'answer': 'Searching algorithms are used to find a specific item or element in a collection of data, while sorting algorithms arrange the elements in a specific order.'}

```
 - """Follow my instructions precisely. Everytime you receive an input list in the format:
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
    [['Introduction to Quantum Computing', 'History and motivations', 'Basics of quantum mechanics', 'Qubits and quantum gates', 'Quantum superposition and measurement', 'Quantum entanglement'], ['Quantum Circuits and Algorithms', 'Quantum gates and their operations', 'Quantum circuits', 'Quantum oracles', 'Deutsch-Jozsa algorithm', "Grover's algorithm"], ['Quantum Computing Building Blocks', 'Quantum logic gates', 'Quantum Fourier transform', 'Quantum phase estimation', 'Quantum parallelism', 'Preparing quantum states'], ['Quantum Error Correction', 'Introduction to quantum error correction', 'Quantum error models', 'Stabilizer codes', 'Fault-tolerant quantum computing', 'Quantum error correction codes'], ['Quantum Teleportation and Quantum Cryptography', 'Quantum teleportation protocol', 'Quantum key distribution', 'Quantum cryptography protocols', 'EPR paradox', 'BB84 protocol'], ['Quantum Simulation and Quantum Annealing', 'Quantum simulation methods', 'Adiabatic quantum computing', 'Quantum annealing', 'Quantum adiabatic theorem', 'D-Wave quantum annealer'], ['Quantum Algorithms and Applications', "Shor's algorithm", 'Factoring large numbers', 'Quantum phase estimation', 'Quantum machine learning', 'Quantum optimization'], ['Current Challenges and Future Perspectives', 'Current state of quantum computers', 'Challenges in scaling up quantum computers', 'Quantum supremacy', 'Applications of quantum computing in various fields', 'Future prospects of quantum computing']]
```
['Introduction to Quantum Computing', 'History and motivations', 'Basics of quantum mechanics', 'Qubits and quantum gates', 'Quantum superposition and measurement', 'Quantum entanglement']
{'question': 'How do qubits and quantum gates relate to Quantum Computing?', 'answer': 'Qubits are the basic units of information in Quantum Computing, similar to classical bits. Quantum gates are mathematical operations that manipulate the state of qubits, allowing for computation.'}   
['Quantum Circuits and Algorithms', 'Quantum gates and their operations', 'Quantum circuits', 'Quantum oracles', 'Deutsch-Jozsa algorithm', "Grover's algorithm"]
{'question': "What is Grover's algorithm?", 'answer': "Grover's algorithm is a quantum search algorithm that can find the solution to an unsorted database with a quadratic speedup compared to classical search algorithms."}
['Quantum Computing Building Blocks', 'Quantum logic gates', 'Quantum Fourier transform', 'Quantum phase estimation', 'Quantum parallelism', 'Preparing quantum states']
{'question': 'What is the quantum Fourier transform?', 'answer': 'The quantum Fourier transform is a quantum algorithm that converts the representation of a quantum state from the time domain to the frequency domain, similar to the classical Fast Fourier Transform (FFT).'}
['Quantum Error Correction', 'Introduction to quantum error correction', 'Quantum error models', 'Stabilizer codes', 'Fault-tolerant quantum computing', 'Quantum error correction codes']
{'question': 'What are stabilizer codes?', 'answer': 'Stabilizer codes are a type of quantum error correction code that can detect and correct errors in quantum information.'}
['Quantum Teleportation and Quantum Cryptography', 'Quantum teleportation protocol', 'Quantum key distribution', 'Quantum cryptography protocols', 'EPR paradox', 'BB84 protocol']
{'question': 'What is quantum key distribution?', 'answer': 'Quantum key distribution is a method of securely distributing encryption keys using the principles of quantum mechanics to ensure the keys cannot be intercepted without detection.'}
['Quantum Simulation and Quantum Annealing', 'Quantum simulation methods', 'Adiabatic quantum computing', 'Quantum annealing', 'Quantum adiabatic theorem', 'D-Wave quantum annealer']
{'question': 'What is adiabatic quantum computing?', 'answer': 'Adiabatic quantum computing is a model of quantum computation based on the adiabatic theorem of quantum mechanics.'}
['Quantum Algorithms and Applications', "Shor's algorithm", 'Factoring large numbers', 'Quantum phase estimation', 'Quantum machine learning', 'Quantum optimization']
{'question': 'What is quantum optimization?', 'answer': 'Quantum optimization is the application of quantum computing techniques to solve optimization problems more efficiently than classical methods.'}
['Current Challenges and Future Perspectives', 'Current state of quantum computers', 'Challenges in scaling up quantum computers', 'Quantum supremacy', 'Applications of quantum computing in various fields', 'Future prospects of quantum computing']
{'question': 'What are the future prospects of quantum computing?', 'answer': 'The future prospects of quantum computing include solving complex problems with speed and efficiency, revolutionizing various industries, and advancing scientific research.'}

```