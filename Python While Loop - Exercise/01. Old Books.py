wanted_book = str(input())

searched_books_counter = 0
while True:
    book_entry = str(input())
    if book_entry == "No More Books":
        print(f"The book you search is not here!"
              f"\nYou checked {searched_books_counter} books.")
        break
    if book_entry == wanted_book:
        print(f"You checked {searched_books_counter} books and found it.")
        break
    searched_books_counter += 1
