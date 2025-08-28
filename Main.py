
def quiz():
    
    
    correctAnswers = 0
    totalQuestions = 3
    Options = ["A","B","C"]
    Guess = 0
    firstGuess = 0
    #Q1I = question one information
    # format = [question, option A, option B, option C, answer] 
    Q1I = ["Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?","Delete the message and try to forget about it","Keep the text and show an adult you trust","Text the person back saying something mean to them","B"]
    Q2I = ["You find out that someone has posted an embarrassing picture of you online. What should you do?","Tweet that they are an idiot and a loser","Ask your friends to give the person a hard time","Tell an adult you trust","C"]
    Q3I = ["You want to join an online gaming site. Which of the following information is okay for you to post on the site.","A nickname","Your name","Your email address","A"]

    #getting username
    username = input("Input Username: ")

    #checking if under correct age
    while True:
        age = -1
        try:
            age = int(input("Input Age: "))
            if age < 100:
                if age > 13:
                    input("You are older than the recommended age category, we recommend you try out our \"Cybersmart Youth Quiz\" if you wish to continue press enter")
                else:
                    input("You are in the recommended age category, press enter to start.")
                print("\n" * 20)
                break
            else:
                print("Invalid age, Please only use numbers 1-100")             
        except ValueError:
            print("Invalid age, Please only use numbers 1-101")

    
    #asking question 1
    for i in range(3):
        #printing question 1
        print(Q1I[0])
        print("A: ",Q1I[1])
        print("B: ",Q1I[2])
        print("C: ",Q1I[3])
        #getting users guess and checking if its A B or C
        
        #checking the the input is a valid option
        while Guess not in Options:
            if firstGuess == 1:
                print("invalid input, please try again")
            firstGuess = 1
            Guess = input("Please answer the question with A B or C: ").upper()

        #checking if guess is correct and checking if it was on the first try
        if Guess == Q1I[4]:
            if i == 0:
                input(f"Thats correct {username}! you have gained 1 point for getting it correct on your first try, press enter to continue.")
                correctAnswers += 1
                print("\n" * 20)
                break
            else:
                input(f"Thats correct {username}! press enter to continue.")
                print("\n" * 20)
                break
            #checking if this is the 3rd time getting it wrong
        else:
                if i == 2:
                    input(f"Sorry that is incorrect, the correct answer was {Q1I[4]} and due to getting the question wrong three times in a row it will be skipped, please press enter to continue")
                    print("\n" * 20)
                else:
                    input("Sorry that is incorrect, please press enter to try again")
                    print("\n" * 20)
        #resetting guess and first guess for next question
        firstGuess = 0
        Guess = 0
                    
    #asking question 2
    for i in range(3):
        #printing question 2
        print(Q2I[0])
        print("A: ",Q2I[1])
        print("B: ",Q2I[2])
        print("C: ",Q2I[3])
        #getting users guess and checking if its A B or C
        
        #checking the the input is a valid option
        while Guess not in Options:
            if firstGuess == 1:
                print("invalid input, please try again")
            firstGuess = 1
            Guess = input("Please answer the question with A B or C: ").upper()

        #checking if guess is correct and checking if it was on the first try
        if Guess == Q2I[4]:
            if i == 0:
                input(f"Thats correct {username}! you have gained 1 point for getting it correct on your first try, press enter to continue.")
                correctAnswers += 1
                print("\n" * 20)
                break
            else:
                input(f"Thats correct {username}! press enter to continue.")
                print("\n" * 20)
                break
            #checking if this is the 3rd time getting it wrong
        else:
                if i == 2:
                    input(f"Sorry that is incorrect, the correct answer was {Q1I[4]} and due to getting the question wrong three times in a row it will be skipped, please press enter to continue")
                    print("\n" * 20)
                else:
                    input("Sorry that is incorrect, please press enter to try again")
                    print("\n" * 20)
        #resetting guess and first guess for next question
        firstGuess = 0
        Guess = 0
                            
    #asking question 1
    for i in range(3):
        #printing question 1
        print(Q3I[0])
        print("A: ",Q3I[1])
        print("B: ",Q3I[2])
        print("C: ",Q3I[3])
        #getting users guess and checking if its A B or C
        
        #checking the the input is a valid option
        while Guess not in Options:
            if firstGuess == 1:
                print("invalid input, please try again")
            firstGuess = 1
            Guess = input("Please answer the question with A B or C: ").upper()

        #checking if guess is correct and checking if it was on the first try
        if Guess == Q3I[4]:
            if i == 0:
                input(f"Thats correct {username}! you have gained 1 point for getting it correct on your first try, press enter to continue.")
                correctAnswers += 1
                print("\n" * 20)
                break
            else:
                input(f"Thats correct {username}! press enter to continue.")
                print("\n" * 20)
                break
            #checking if this is the 3rd time getting it wrong
        else:
                if i == 2:
                    input(f"Sorry that is incorrect, the correct answer was {Q1I[4]} and due to getting the question wrong three times in a row it will be skipped, please press enter to continue")
                    print("\n" * 20)
                else:
                    input("Sorry that is incorrect, please press enter to try again")
                    print("\n" * 20)
        #resetting guess and first guess for next question
        firstGuess = 0
        Guess = 0
        
    #printing score
    print("you scored ", correctAnswers, " out of ", totalQuestions)
                    

quiz()