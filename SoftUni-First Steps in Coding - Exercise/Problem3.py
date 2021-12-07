sum_money = float(input())
period = int(input())
interest = float(input())

percentage_interest = interest / 100
yearly_interest = sum_money * percentage_interest
monthly_interest = yearly_interest / 12
total_sum_of_money = monthly_interest * period + sum_money

print(total_sum_of_money)