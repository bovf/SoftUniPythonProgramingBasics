story = int(input())
rooms = int(input())
story_counter = 0
for a in range(story, 0, -1):
    for i in range(0, rooms):
        if a == story:
            print(f"L{a}{i} ", end="")
        else:
            if a % 2 == 0:
                print(f"O{a}{i} ", end="")
            else:
                print(f"A{a}{i} ", end="")
        if i == rooms - 1:
            print("")
            break
