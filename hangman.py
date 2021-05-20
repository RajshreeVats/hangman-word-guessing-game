import random

 
name = input("What is your name? ")
 
print("Let's start ! ", name)
 
from words import words
 

word = random.choice(words)
 
 
print("Guess the characters")
 
guesses = ''
 
turns = 12
 
 
while turns > 0:
     
    # counts the number of times failed input
    failed = 0
     

    for char in word:
         
        
        if char in guesses:
            print(char)
             
        else:
            print("_")
             
        
            failed += 1
             
 
    if failed == 0:
        print("You Win")
         
    
        print("The word is: ", word)
        break
     
    # if user has input the wrong alphabet 
    guess = input("guess a character:")
     

    guesses += guess
     
    #check if input word is in list
    if guess not in word:
         
        turns -= 1
         
        
        print("Wrong")
         
        
        print("You have", + turns, 'more guesses')
         
         
        if turns == 0:
            print("You Loose")