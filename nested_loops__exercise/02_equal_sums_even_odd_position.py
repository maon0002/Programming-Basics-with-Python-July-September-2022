first_number = int(input())
second_number = int(input())
sum_even_positions = 0
sum_odd_positions = 0
is_odd_equal_even = False

for current_number in range(first_number, second_number + 1):
    for position in range(6):
        current_number_str = str(current_number)
        # current_position = position
        if position % 2 == 0:
            sum_odd_positions += int(current_number_str[position])
        else:
            sum_even_positions += int(current_number_str[position])

    if sum_odd_positions == sum_even_positions:
        is_odd_equal_even = True  # after this we must print
        print(f"{current_number}", end=" ")
        # break
    sum_even_positions = 0
    sum_odd_positions = 0


