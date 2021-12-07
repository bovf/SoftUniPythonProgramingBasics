n = int(input())

even_sum = 0
odd_sum = 0
counter_pos = 1

for a in range(0, n):
    number = int(input())
    if counter_pos % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
    counter_pos += 1
if even_sum == odd_sum:
    print(f"Yes\nSum = {even_sum}")
else:
    print(f"No\nDiff = {abs((even_sum - odd_sum))}")
