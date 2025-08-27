"""What the program needs to do
At the start of the game, get the users name and use their name throughout the game (where appropriate).
The game is designed for children from 8 to 13 years of age.
If the child is older (14 years plus) they should be encouraged to try the Cybersmart Youth Quiz instead. 
Note: You do not need to create the Cybersmart Youth Quiz.

Questions and answers
The program should include at least three questions. 
The questions and their correct answers should be stored in lists in your program.
Examples of questions and answers for the quiz are on the next page. 

Scoring
If the child gets the answer correct the first time, they get one point for the question.
If they get the answer wrong, they should be encouraged to try again – two more times 
(ie a total of three tries). If they still can’t get it right, they are told the correct answer, 
and move on to the next question.

Important: They only get a point for a question if they get it correct the first time they try.
At the end of the quiz the child should be given their score (ie the number of questions they got right on their first try).
"""
def quiz():
    
    
    correctAnswers = 0
    totalQuestions = 3
    #Q1I = question one information
    # format = [question, option A, option B, option C, answer] 
    Q1I = ["Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?","Delete the message and try to forget about it","Keep the text and show an adult you trust","Text the person back saying something mean to them","B"]
    Q2I = ["You find out that someone has posted an embarrassing picture of you online. What should you do?","Tweet that they are an idiot and a loser","Ask your friends to give the person a hard time","Tell an adult you trust","C"]
    Q3I = ["You want to join an online gaming site. Which of the following information is okay for you to post on the site.","A nickname","Your name","Your email address","A"]

    #getting username
    username = input("Input Username: ")

    #checking if under correct age
    age = int(input("Input Age: "))
    if age > 13:
        print("You are older than the recommended age category, we recommend you try out our \"Cybersmart Youth Quiz\" instead.")
        quit()
    else:
        _ = input("You are in the recommended age category, press enter to start.")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
        #asking question 1
        for i in range(3):
            print(Q1I[0])
            print("A: ",Q1I[1])
            print("B: ",Q1I[2])
            print("C: ",Q1I[3])
            Guess = input("Please answer the question with A B or C: ").upper()
            if Guess == Q1I[4]:
                if i == 0:
                    _ = input("Thats correct! you have gained 1 point for getting it correct on your first try, press enter to continue.")
                    correctAnswers += 1
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    break
                else:
                    _ = input("Thats correct! press enter to continue.")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    break
            else:
                    if i == 2:
                        _ = input("Sorry that is incorrect, due to getting the question wrong three times in a row it will be skipped, please press enter to continue")
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    else:
                        _ = input("Sorry that is incorrect, please press enter to try again")
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        
        #asking question 2
        for i in range(3):
            print(Q2I[0])
            print("A: ",Q2I[1])
            print("B: ",Q2I[2])
            print("C: ",Q2I[3])
            Guess = input("Please answer the question with A B or C: ").upper()
            if Guess == Q2I[4]:
                if i == 0:
                    _ = input("Thats correct! you have gained 1 point for getting it correct on your first try, press enter to continue.")
                    correctAnswers += 1
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    break
                else:
                    _ = input("Thats correct! press enter to continue.")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    break
            else:
                    if i == 2:
                        _ = input("Sorry that is incorrect, due to getting the question wrong three times in a row it will be skipped, please press enter to continue")
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    else:
                        _ = input("Sorry that is incorrect, please press enter to try again")
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        
        #asking question 3
        for i in range(3):
            print(Q3I[0])
            print("A: ",Q3I[1])
            print("B: ",Q3I[2])
            print("C: ",Q3I[3])
            Guess = input("Please answer the question with A B or C: ").upper()
            if Guess == Q3I[4]:
                if i == 0:
                    _ = input("Thats correct! you have gained 1 point for getting it correct on your first try, press enter to continue.")
                    correctAnswers += 1
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    break
                else:
                    _ = input("Thats correct! press enter to continue.")
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    break
            else:
                    if i == 2:
                        _ = input("Sorry that is incorrect, due to getting the question wrong three times in a row it will be skipped, please press enter to continue")
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    else:
                        _ = input("Sorry that is incorrect, please press enter to try again")
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        
        print("you scored ", correctAnswers, " out of ", totalQuestions)
                        

quiz()