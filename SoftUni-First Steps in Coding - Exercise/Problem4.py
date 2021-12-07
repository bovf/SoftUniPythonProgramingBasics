number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

time_needed_for_the_book = number_of_pages / pages_per_hour
hours_needed_per_day = time_needed_for_the_book / number_of_days
print(hours_needed_per_day)
