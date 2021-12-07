width = int(input())
height = int(input())
length = int(input())

volume = width * height * length
free_space = volume

while True:
    entry = str(input())
    if entry == "Done":
        print(f"{free_space} Cubic meters left.")
        break
    if free_space - int(entry) < 0:
        print(f"No more free space! You need {(abs(free_space - int(entry)))} Cubic meters more.")
        break
    free_space -= int(entry)
