number = int(input())
special_counter = 0

for current_number in range(1111, 10000):
    for position in range(4):
        # current_position = str(position)
        current_number = str(current_number)
        divider = current_number[position]
        divider = int(divider)

        if divider == 0:
            special_counter = 0
            break
        elif number % divider == 0:
            special_counter += 1
        else:
            special_counter = 0
            break

        if special_counter == 4:
            print(current_number, end=" ")
            special_counter = 0
