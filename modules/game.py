from modules.player import Player

class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


    def compare(self):
        if self.player1.choice == self.player2.choice:
            return "No one"
        elif self.player1.choice == 'rock' and self.player2.choice == "scissors":
            return self.player1.name
        elif self.player1.choice == 'paper' and self.player2.choice == "rock":
            return self.player1.name
        elif self.player1.choice == 'scissors' and self.player2.choice == "paper":
            return self.player1.name
        else:
            return self.player2.name