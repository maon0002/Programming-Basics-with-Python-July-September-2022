fav_book = input()
book = ""
search_counter = 0
founded = False

while True:
    book = input()
    if book != "No More Books":

        if fav_book == book:
            founded = True
            # search_counter += 0
            break
        else:
            search_counter += 1
    else:
        break

if founded:
    print(f"You checked {search_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {search_counter} books.")
