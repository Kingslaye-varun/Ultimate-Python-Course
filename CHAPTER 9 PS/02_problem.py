import random

def game():
    print("You are playing the game")

    score = random.randint(1,50)
    
    with open("highScore.txt") as f:
        highScore = f.read()
        if(highScore != ""):
            highScore = int(highScore)
        else:
            highScore = 0
    
    print(f"Your Score: {score}")
    if(score>highScore):
        with open("highScore.txt", "w") as f:
            f.write(str(score))
        
    return score    

game()