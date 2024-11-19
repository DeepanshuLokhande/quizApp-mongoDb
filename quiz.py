from dbConnection import signUp, logIn
from quetions import quiz

userdata = input('press 1 to sign up or 2 to login: ')
if userdata == '1':
    userName = input('Enter your username: ')
    if not userName:
        print("Username cannot be empty.")
    else:
        password = input('Enter your password: ')
        city = input('Enter your city: ')
        signUp(userName, city, password)
        quiz()
        
elif userdata == '2':
    userName = input('Enter your username: ')
    password = input('Enter your password: ')
    logIn(userName, password)
    quiz()