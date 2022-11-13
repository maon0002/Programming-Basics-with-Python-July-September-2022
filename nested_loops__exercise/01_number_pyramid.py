number = int(input())
number_for_print = 0
is_reached = False

for rows in range(1, number + 1):
    for columns in range(1, rows + 1):
        number_for_print += 1
        print(f"{number_for_print}", end=" ")

        if number_for_print == number:
            is_reached = True
            break
    print()
    if is_reached:
        break
