import random

class Player():
    """This game simulates the classic Rock-Paper-Scissors game, defaulting to the computer as your opponent. 
    However, the code allows modification should you want to include an option for a remote human opponent. """
    choices = ["rock", "paper", "scissors"]
    def __init__(self):
        self.choice = ""
    
    def playRPS(self, player_comp):
        if self.choice.lower() not in Player.choices or player_comp.choice.lower() not in Player.choices:
            print("That is not a valid choice.")
            return
        if isinstance(player_comp, compPlayer):
            print(f"The computer's choice is {player_comp.choice}.")
        else:
            print(f"The other player's choice is {player_comp.choice}.")
        if self.choice == player_comp.choice:
            print('Game Tied')
        elif self.choice.lower() == "rock" and player_comp.choice.lower() == "paper":
            print("You lose")
        elif self.choice.lower() == "scissors" and player_comp.choice.lower() == "rock":
            print("You loose")
        elif self.choice.lower() == "paper" and player_comp.choice.lower() == "scissors":
            print("You lose")
        else:
            print("You win")
    
    def continuousPlay(self, opponent):
        while True:
            self.choice = input("Please type your choice of either 'rock' 'paper' or 'scissors' (To quit, type 'I quit'):  ")
            if self.choice.lower() == "i quit":
                print("Thank you for playing")
                break
            # if want to add a human opponent, include an additional line here to retreive a self.choice value remotely
            self.playRPS(opponent)
            if isinstance(opponent, compPlayer):
                opponent.choice = random.choice(Player.choices)
                
class compPlayer(Player):
    """this subclass defines a computer player"""
    def __init__(self):
        self.choice = random.choice(Player.choices)

class humanPlayer(Player):
    """this subclass would define a remote human opponent for future expansion of the game"""
    pass


print("Welcome to the Rock, Paper, Scissors Game!")
my_player = Player()
computer_player = compPlayer()

my_player.continuousPlay(computer_player)