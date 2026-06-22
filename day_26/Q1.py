import random 
class Guessnumber:
    def __init__(self):
        
        self.num = random.randint(1,50)
    def quiz(self):
        while True:   
            a = int(input("enter your number"))
            
            if a > self.num:                
                print("Guess lower")               
            elif a < self.num:       
                print("guess uper")
            else:
                print("congratulation you guess the number")
                break
game = Guessnumber()
game.quiz()
