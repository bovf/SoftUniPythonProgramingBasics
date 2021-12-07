cake_width = float(input())
cake_length = float(input())

cake_size = cake_width * cake_length
cake_pieces = cake_size / 1
cake_left = cake_pieces
while True:
    if cake_left <= 0:
        print(f"No more cake left! You need {(abs(cake_left)):.0f} pieces more.")
        break
    else:
        piece_entry = input()
        if piece_entry == "STOP":
            print(f"{cake_left:.0f} pieces are left.")
            break
        else:
            cake_left -= float(piece_entry)
