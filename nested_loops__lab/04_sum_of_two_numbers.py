start_range = int(input())
end_range = int(input())
magic_number = int(input())
counter = 0
is_equal = False

for x in range(start_range, end_range + 1):

    for y in range(start_range, end_range + 1):
        counter += 1
        if x + y == magic_number:
            is_equal = True
            break
    if is_equal:
        break

if is_equal:
    print(f"Combination N:{counter} ({x} + {y} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")
