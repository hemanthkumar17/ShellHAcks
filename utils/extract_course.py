import json

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


def main():
    
  groups=[]
  for i in response:
     groups.append(response[i])

if __name__=="__main__":
    main()