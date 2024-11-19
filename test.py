import random

def allQuestion(filename):
    questions = []
    try:
        with open(f"./questions/{filename}", 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3): 
                question_text = lines[i].strip()
                options = lines[i+1].strip().split(',')
                # print(options)
                answer = lines[i+2].strip()
                questions.append({
                    "question": question_text,
                    "options": options,
                    "answer": str(answer)
                })
            # print(questions)
            # print(len(questions))
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return questions

def getQuestion(questions, no_of_questions=5):
    return random.sample(questions, no_of_questions)

def quiz():
    score = 0
    topic = input("Please enter the topic you want to take the quiz on: 1 for Java, 2 for Python, 3 for RDBMS: ")
    
    if topic == '1':
        print("Welcome to the Java quiz")
        java_questions = allQuestion('java_questions.txt')
        questions = getQuestion(java_questions)
        
    elif topic == '2':
        print("Welcome to the Python quiz")
        python_questions = allQuestion('python_questions.txt')
        questions = getQuestion(python_questions)
        
    elif topic == '3':
        print("Welcome to the RDBMS quiz")
        rdbms_questions = allQuestion('rdbms_questions.txt')
        questions = getQuestion(rdbms_questions)
    
    else:
        print("Invalid option. Exiting quiz.")
        return

    # Display and handle quiz questions
    for i, question in enumerate(questions):
        print(f"{i+1}. {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"{j+1}. {option}")
        answer = int(input("Enter your answer: "))
        if question['options'][answer-1] == question['answer']:
            print("Correct answer")
            score += 1
        else:
            print("Incorrect answer")
    
    print(f"Your score is {score}")
