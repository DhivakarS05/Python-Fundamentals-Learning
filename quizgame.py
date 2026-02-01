questions = (("1.What is 2+2?"),
             ("2.What is 10/2?"),
             ("3.What is 5*10?"),
             ("4.What is 10-15?"))
options = (("A.3","B.5","C.4","D.22"),
          ("A.10","B.2","C.5","D.1"),
          ("A.50","B.10","C.4","D.22"),
          ("A.3","B.5","C.4","D.22"),)
answers=("C","C","A","B")
guesses=[]
question_no = 0
score = 0

for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_no]:
        print(option)
    guess = input("Enter option A,B,C,D: ").upper()
    guesses.append(guess)
    if guess == answers[question_no]:
        score +=1
        print("Correct!")
    else:
        print("Incorrect!")
    question_no +=1
print("-------your guess-------")
for i in guesses:
    for j in i:
        print(j,end=" ")
print()
print("-------Correct answer-------")
for i in answers:
    for j in i:
        print(j,end=" ")
print()
print(int(score/len(questions)*100),"%")