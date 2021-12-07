student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while True:
    entry = input()
    if entry == "Finish":
        break
    else:
        max_capacity = int(input())
        seats_taken = 0
        while max_capacity > seats_taken:
            ticket_entry = input()
            if ticket_entry == "End":
                break
            else:
                seats_taken += 1
                if ticket_entry == "student":
                    student_tickets += 1
                if ticket_entry == "kid":
                    kids_tickets += 1
                if ticket_entry == "standard":
                    standard_tickets += 1
        print(f"{entry} - {(seats_taken / max_capacity * 100):.2f}% full.")

tickets_sold = kids_tickets + standard_tickets + student_tickets

print(f"Total tickets: {tickets_sold}")
print(f"{(student_tickets / tickets_sold * 100):.2f}% student tickets.")
print(f"{(standard_tickets / tickets_sold * 100):.2f}% standard tickets.")
print(f"{(kids_tickets / tickets_sold * 100):.2f}% kids tickets.")
