# from pymongo import MongoClient
from dbConnection import db
import random
# Connect to MongoDB
# client = MongoClient("mongodb+srv://deepanshulokhande5:Deepanshulokhande15052004@cluster0.66her.mongodb.net/")
# db = client["Cluster0"]
def getQuestion(questions, no_of_questions=5):
    return random.sample(questions, no_of_questions)

def quiz():
    topic = input("Please enter the topic you want to take the quiz on: 1 for Java, 2 for Python, 3 for RDBMS: ")
    # all_questions;
    if topic == "1":
        collection = db["java"]
        all_questions = list(collection.find({}))
        question= getQuestion(all_questions)
    elif topic =="2":
        collection = db["python"]
        all_questions = list(collection.find({})) 
        question= getQuestion(all_questions)
    elif topic =="3":
        collection = db["rdbms"]
        all_questions = list(collection.find({})) 
        question= getQuestion(all_questions)
    else:
        print("Invalid topic selected.")
        return

    # Print or process the selected questions
    score = 0 
    for i, question in enumerate(question):
            print(f"{i+1}. {question['question']}")
            for j, option in enumerate(question['options']):
                print(f"{j+1}. {option}")
            answer = int(input("Enter your answer: "))
            if question['options'][answer-1] == question['answer']:
                score +=1
                print("Correct answer")
            else:
                print("Incorrect answer")
    print(f"your Score is {score}.")

