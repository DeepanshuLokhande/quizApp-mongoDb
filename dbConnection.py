# from quetions import random_questions
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://deepanshulokhande5:Deepanshulokhande15052004@cluster0.66her.mongodb.net/")
db = client["Cluster0"]
users_collection = db["test"]

# Signup function
def signUp(userName, city, password):
    if not userName:
        print("Username cannot be empty.")
        return False
    if users_collection.find_one({"userName": userName}):
        print("User already exists. Please use a different username.")
        return False
    user_data = {
        "userName": userName,
        "city": city,
        "password": password,
    }
    users_collection.insert_one(user_data)
    print("Signup successful!")
    return True

# Login function
def logIn(userName, password):
    user = users_collection.find_one({"userName": userName, "password": password})
    if user:
        print("Login successful!")
        
    else:
        print("Invalid username or password.")
        return False