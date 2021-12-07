import sys

min_num = sys.maxsize
while True:
    n = (input())
    if str(n) == "Stop":
        print(min_num)
        break
    if int(n) < min_num:
        min_num = int(n)
