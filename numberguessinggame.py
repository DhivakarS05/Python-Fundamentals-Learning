import random

low = 1
high = 100
guesses = 0
number = random.randint(low,high)
print("Number guessing game")
print(f"Enter a number between {low} to {high}")
print(number)

while True:
    guess = int(input("Enter your guessing number: "))
    guesses +=1
    if guess>high or guess<low:
        print("out of range")
    elif guess>number:
        print("Too High")
    elif guess<number:
        print("Too low")
    else:
        print("CORRECT!!!")
        break
print(f"Number of guesses you taken is {guesses}")