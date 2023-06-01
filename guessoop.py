import random


class trivia:
    def __init__(self):
        self.number = random.randint(1, 10)
        self.user_guess = int(input("Kindly guess a number between 1 and 10: "))
        self.chance = 5
     
    
        
    def check_user_guess(self):
        while self.chance !=0:
            if self.user_guess !=self.number:
                self.chance -= 1
                if self.user_guess < self.number and self.chance != 0:
                    print("Your guess is  lower than the number") 
                    print(f"you have {self.chance} chances left ")
                    self.user_guess = int(input("Kindly guess a higher number: "))
                elif self.user_guess > self.number and self.chance != 0:
                    print("Your guess is higher than number")
                    print(f"you have {self.chance} chances left ")
                    self.user_guess = int(input("Kindly guess a lower number: "))
            else:
                print(f"user_guessed no {self.user_guess} is correct")
                self.chance = 0
        if self.user_guess !=self.number and self.chance == 0:
            print("You have exhausted your chances")
            self.chance = 0
            
            
        
        
quest=trivia()
quest.check_user_guess()