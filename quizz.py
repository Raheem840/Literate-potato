questions = ("How many continents are there in the world?",
             "Which element has atomic number 1?",
             "What is the capital city of USA?",
             "Who has the most ballon dors?"
             )
options = (("A.3", "B.7", "C.8","D.20"),
           ("A.Oxygen","B.Nitrogen","C.hydrogen","D.Flourine"),
           ("A.Detroit","B.Wahington D.C","C.Texas","D.New York"),
           ("A.L.Messi","B.C.Ronaldo","C.Neymar Jr","D.O.Dembele"))
answers = ("B","C","B","A")  #answers to the quizz
guesses =[]  #list to store our user's answers to the questions
score = 0
question_num = 0

for question in questions:
    print("--------------")
    print(question)

    for option in options[question_num]:
        print(option)
    guess = input("Choose your answer: A,B,C,D ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score +=1
        print("CORRECT")
    else :
        print("INCORRECT")
        print(f"The correct answer is {answers[question_num]}")
    question_num +=1
print("---------")
print("RESULTS")
print("Answers: ", end="")
#iterate through the answers
for answer in answers:
    print(answer, end=" ")
print()
#iterate through the guesses
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions)*100)
print(f"Your score is {score}%")

