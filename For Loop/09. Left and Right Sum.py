n = int(input())

n_times_2 = n * 2
n_left = 0
n_left_sum = 0
for a in range(0, n):
    n_left = int(input())
    n_left_sum += n_left
n_right = 0
n_right_sum = 0
for a in range(0, n):
    n_right = int(input())
    n_right_sum += n_right

if n_right_sum == n_left_sum:
    print(f"Yes, sum = {n_right_sum}")
else:
    print(f"No, diff = {abs((n_right_sum - n_left_sum))}")