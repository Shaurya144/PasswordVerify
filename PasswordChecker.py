# in this piece of code, we get the users input for thier password and check if it is a weak password or a 
# reliable one. First we get an input for their passwords, then we check if it is less than 8 characters 
# and if they have an integer as their first character. If so, then i will assign them a new password and 
# ask them to verify the password.

import time

def checkPassword(userPassword):
    if len(userPassword) > 8 and userPassword[0] != int:
        print("Great password! Now let's verify")
        time.sleep(2)
        UserAttemptOne = input("What is your password - Attempt 1 : ")
        if UserAttemptOne == userPassword:
            time.sleep(1)
            UserAttemptTwo = input("What is your password - Attempt 2 : ")
            if UserAttemptTwo == userPassword:
                print("Well done! You have a strong password and you know it well!")
            else:
                print("XXXX THAT'S WRONG XXXX")
        else:
                print("XXXX THAT'S WRONG XXXX")

    elif len(userPassword) <= 8 and userPassword[0] != int:
        print("Please use more than 8 characters ")
        userPassword = "potato123" # thisisanicepassword
        print(userPassword + " this is your new password, learn it and now lets verify")
        time.sleep(3)
        UserAttemptOne = input("What is your password - Attempt 1 : ")
        if UserAttemptOne == userPassword:
            time.sleep(1)
            UserAttemptTwo = input("What is your password - Attempt 2 : ")
            if UserAttemptTwo == userPassword:
                print("Well done! You have a strong password and you know it well!")
            else:
                print("XXXX THAT'S WRONG XXXX")
        else:
                print("XXXX THAT'S WRONG XXXX")
        return userPassword
    
    elif len(userPassword) > 8 and userPassword[0] == int:
        print("Please do not use an integer as your first character")
        userPassword = "potato123" # thisisanicepassword
        print(userPassword + " this is your new password, learn it and now lets verify")
        time.sleep(3)
        UserAttemptOne = input("What is your password - Attempt 1 : ")
        if UserAttemptOne == userPassword:
            time.sleep(1)
            UserAttemptTwo = input("What is your password - Attempt 2 : ")
            if UserAttemptTwo == userPassword:
                print("Well done! You have a strong password and you know it well!")
            else:
                print("XXXX THAT'S WRONG XXXX")
        else:
                print("XXXX THAT'S WRONG XXXX")
        return userPassword
    else:
        print("An error occured")

userInput= input("Hello Employee, what is your password? ")
time.sleep(3)
checkPassword(userPassword=userInput)
 