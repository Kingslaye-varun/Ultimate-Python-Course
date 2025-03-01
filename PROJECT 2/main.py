import random
n = random.randint(1,100)
num = -1
guesses = 1
while(num != n):
    
    num = int(input("Guess a Number: "))
    
    if(num > n):
        print("Lower Number please")
        guesses += 1
        
    elif(num < n):
        print("Higher Number please")
        guesses += 1
        
print(f"You have guessed the Number {n} in {guesses} attempts")
    