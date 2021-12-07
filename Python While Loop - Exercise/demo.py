print("Welcome to Rock, Paper or Scissors!")
options = ["rock", "paper", "scissors"]
name_p_1 = input("Player 1, what is your name? ")
name_p_2 = input("Player 2, what is your name? ")


def place_your_bets():
    hand_p_1 = input(f"Okay {name_p_1}, enter your hand (Rock, Paper or Scissors): ")
    hand_p_1 = check_input(hand_p_1, name_p_1)
    hand_p_2 = input(f"Okay {name_p_2}, enter your hand (Rock, Paper or Scissors): ")
    hand_p_2 = check_input(hand_p_2, name_p_2)
    return hand_p_1, hand_p_2


def check_input(which_hand, which_name):
    while which_hand.lower() not in options:
        print("Error! Invalid input."
              "\nTry again, enter 'Rock', 'Paper' or 'Scissors'.")
        which_hand = input(f"Okay {which_name}, enter your hand (Rock, Paper or Scissors): ")
    return which_hand


choice_player_1, choice_player_2 = place_your_bets()
print(choice_player_1)
print(choice_player_2)
