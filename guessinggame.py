#Guessing game
import random

print("Hello, what is your name?")
name= input()

print("Hi " + name + " I'm thinking of a random number between 1 to 20 ")
secretnumber = random.randint(1,20)

for guesstaken in range(1,7):
    print("Take a guess:")
    guess=int(input())
    if guess > secretnumber:
        print("Your guess is too high")
    elif guess < secretnumber:
        print("Your guess is too low")
    else:
        break

if guess == secretnumber:
    print('Congrats '+name +" you guessed the number in "+str(guesstaken)+" guesses")
else:
    print("Nope ,The number i was thinking of was "+str(secretnumber))




