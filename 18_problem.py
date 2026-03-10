n = int(input("enter a number :"))
fact = 1 
for i in range (1,n+1):
    fact = fact*fact

# short game 
import random

n = random.randint(1, 50)
attempt = 0

while True:
    num = int(input("Guess a number: "))
    attempt += 1

    if num > n:
        print("Enter a smaller number")
    elif num < n:
        print("Enter a greater number")
    else:
        print("You guessed the right number 🎉")
        print("Total attempts:", attempt)
        break
