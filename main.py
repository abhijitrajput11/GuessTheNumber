import random
def numguess():
    
    number = random.randint(1,100)
    attempts=0
    
    print("welcome to the number guessing game")
    print("you are having 7 attempts")
    print("guess the number between 1 to 100")
   
    while attempts<7:
        
        guess = int (input ("take a Guess"))
        attempts+=1
        
        if guess<number :
            print("too low ! try a higher number")
        elif guess>number:
            print("too high ! try a lower number")
        else:
            print("congratulation ! U guessed the number")
            break
            
    print("number is: ",number)
    print("you loose")
numguess()
