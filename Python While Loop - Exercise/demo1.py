print("Welcome to Rock, Paper or Scissors!")
options = ["rock", "paper", "scissors"]
namep1 = input("Player 1, what is your name? ")
namep2 = input("Player 2, what is your name? ")

def placeyourbets():
    global handp1
    global handp2
    handp1 = input("Okay " + namep1 + ", enter your hand (Rock, Paper or Scissors): ")
    checkinput(handp1, namep1)
    handp2 = input("Okay " + namep2 + ", enter your hand (Rock, Paper or Scissors): ")
    checkinput(handp2, namep2)
    return handp1, handp2
def checkinput(whichhand, whichname):
    while whichhand.lower() not in options:
        print("Error!\nEnter 'rock', 'paper' or 'scissors'.")
        whichhand = input("Okay " + whichname + ", enter your hand (Rock, Paper or Scissors): ")
placeyourbets()