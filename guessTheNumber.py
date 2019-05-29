import random

number = random.randint(1, 10)
tries = 1
username = input("Hi there! would you like to share your username ?")
print("Hello ", username + ".")

question = input("would you like  to play a guessing game with me ? [y/n]")
if question == "n":
    print("Never mind we will play it another  time.. ")

if question == "y":
   print("I am thinking of a number between 1 & 10")
   guess = int(input(" would you like to guess? "))
   if guess > number:
    print("guess lower a bit !!")

   if guess < number:
    print("guess  a bit higher !!")

   while guess != number:
     tries +=  1
     guess = int(input(" incorrect ..try  again !"))

   if guess == number:
    print("Well done..the number was  ", number, " and you have made it with ", tries, "tries")