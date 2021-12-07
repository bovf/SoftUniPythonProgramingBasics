import sys

max_num = -sys.maxsize
while True:
    n = (input())
    if str(n) == "Stop":
        print(max_num)
        break
    if int(n) > max_num:
        max_num = int(n)
