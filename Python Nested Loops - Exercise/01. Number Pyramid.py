n = int(input())

continuity = 1
for a in range(1, n+1):
    for i in range(1, a+1):
        print(f"{continuity} ", end="")
        continuity += 1
        if continuity > n:
            break
    print("")
    if continuity > n:
        break
