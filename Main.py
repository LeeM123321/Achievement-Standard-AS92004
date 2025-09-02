def quiz():
    
    #setting default age and name
    age = -1    
    username = "N/A"
    #defining default correct answers
    correctAnswers = 0
    #defining totalQuestions and questionAttempts static
    totalQuestions = 3
    questionAttempts = 3
    #setting possible question answers
    Options = ["A","B","C"]
    #defining
    Guess = 0
    #Q1I = question one information
    # format = [question, option A, option B, option C, answer] 
    Q1I = ["Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?","Delete the message and try to forget about it","Keep the text and show an adult you trust","Text the person back saying something mean to them","B"]
    Q2I = ["You find out that someone has posted an embarrassing picture of you online. What should you do?","Tweet that they are an idiot and a loser","Ask your friends to give the person a hard time","Tell an adult you trust","C"]
    Q3I = ["You want to join an online gaming site. Which of the following information is okay for you to post on the site.","A nickname","Your name","Your email address","A"]
    print("\n" * 20)
    #getting username
    username = input("Input Username: ").strip()

    #checking is age meets all valid conditions (only contains numbers and is in the range of 1-100 inclusive)
    while True:
        try:
            age = int(input("Input Age: ").strip())
            if age < 101 and age > 0:
                #checking if age is in recommended age range
                if age > 13:
                    #if not in recommended age range then suggesting the cybersmart youth quiz but still letting them continue
                    input("You are older than the recommended age category, we recommend you try out our \"Cybersmart Youth Quiz\" if you wish to continue press enter.\n")
                else:
                    #if in recommended age range then letting them continue normally
                    input("You are in the recommended age category, press enter to start.\n")
                print("\n" * 20)
                break
            else:
                print("Invalid age, Please only use numbers 1-100")
        except ValueError:
            print("Invalid age, Please only use numbers 1-101")

    
    #asking question 1
    #looping for the 3 tries
    for i in range(questionAttempts):
        #printing question 1
        print(Q1I[0])
        print("A: ",Q1I[1])
        print("B: ",Q1I[2])
        print("C: ",Q1I[3])
        #getting users guess and checking if its A B or C
        Guess = input("Please answer the question with A B or C: ").upper()
        #checking the the input is a valid option
        while Guess not in Options:
            #telling the user if it was invalid and letting them guess again
            print("invalid input, please try again.\n")
            Guess = input("Please answer the question with A B or C: ").upper()

        #checking if guess is correct or incorrect 
        if Guess == Q1I[4]:
            #checking if it was correct on the first try
            if i == 0:
                input(f"Thats correct {username}! you have gained 1 point for getting it correct on your first try, press enter to continue.\n")
                #adding one to correct answers variable
                correctAnswers += 1
                print("\n" * 20)
                #exiting loop
                break
            else:
                input(f"Thats correct {username}! press enter to continue.\n")
                print("\n" * 20)
                #exiting loop
                break
        else:
            #checking if this is the 3rd time getting it wrong or not
                if i == questionAttempts -1:
                    input(f"Sorry that is incorrect, the correct answer was {Q1I[4]} and due to getting the question wrong three times in a row it will be skipped, please press enter to continue.\n")
                    print("\n" * 20)
                else:
                    input("Sorry that is incorrect, please press enter to try again.\n")
                    print("\n" * 20)
        #resetting guess for next question
        Guess = 0
                    
    #asking question 2
    #looping for the 3 tries
    for i in range(3):
        #printing question 2
        print(Q2I[0])
        print("A: ",Q2I[1])
        print("B: ",Q2I[2])
        print("C: ",Q2I[3])
        #getting users guess and checking if its A B or C
        Guess = input("Please answer the question with A B or C: ").upper()
        #checking the the input is a valid option
        while Guess not in Options:
            #telling the user if it was invalid and letting them guess again
            print("invalid input, please try again.\n")
            Guess = input("Please answer the question with A B or C: ").upper()

        #checking if guess is correct or incorrect 
        if Guess == Q2I[4]:
            #checking if it was correct on the first try
            if i == 0:
                input(f"Thats correct {username}! you have gained 1 point for getting it correct on your first try, press enter to continue.\n")
                #adding one to correct answers variable
                correctAnswers += 1
                print("\n" * 20)
                #exiting loop
                break
            else:
                input(f"Thats correct {username}! press enter to continue.\n")
                print("\n" * 20)
                #exiting loop
                break
        else:
            #checking if this is the 3rd time getting it wrong or not
                if i == 2:
                    input(f"Sorry that is incorrect, the correct answer was {Q1I[4]} and due to getting the question wrong three times in a row it will be skipped, please press enter to continue.\n")
                    print("\n" * 20)
                else:
                    input("Sorry that is incorrect, please press enter to try again.\n")
                    print("\n" * 20)
        #resetting guess for next question
        Guess = 0
                            
    #asking question 3
    #looping for the 3 tries
    for i in range(3):
        #printing question 3
        print(Q3I[0])
        print("A: ",Q3I[1])
        print("B: ",Q3I[2])
        print("C: ",Q3I[3])
        #getting users guess and checking if its A B or C
        Guess = input("Please answer the question with A B or C: ").upper()
        #checking the the input is a valid option
        while Guess not in Options:
            #telling the user if it was invalid and letting them guess again
            print("invalid input, please try again.\n")
            Guess = input("Please answer the question with A B or C: ").upper()

        #checking if guess is correct or incorrect 
        if Guess == Q3I[4]:
            #checking if it was correct on the first try
            if i == 0:
                input(f"Thats correct {username}! you have gained 1 point for getting it correct on your first try, press enter to continue.\n")
                #adding one to correct answers variable
                correctAnswers += 1
                print("\n" * 20)
                #exiting loop
                break
            else:
                input(f"Thats correct {username}! press enter to continue.\n")
                print("\n" * 20)
                #exiting loop
                break
        else:
            #checking if this is the 3rd time getting it wrong or not
                if i == 2:
                    input(f"Sorry that is incorrect, the correct answer was {Q1I[4]} and due to getting the question wrong three times in a row it will be skipped, please press enter to continue.\n")
                    print("\n" * 20)
                else:
                    input("Sorry that is incorrect, please press enter to try again.\n")
                    print("\n" * 20)
        #resetting guess for next question
        Guess = 0
        
    #printing score based off correctAnswers and totalQuestions
    print("good job ",username,", you scored ", correctAnswers, " out of ", totalQuestions)
quiz()
