k = int(input())
l = int(input())
m = int(input())
n = int(input())

# k = 6
# l = 7
# m = 5
# n = 6
count_changes = 0
enough_changes = False

for first_one in range(k, 8 + 1):

    for first_two in range(9, l - 1, - 1):

        for second_one in range(m, 8 + 1):

            for second_two in range(9, n - 1, - 1):

                if first_one % 2 != 0 or second_one % 2 != 0:
                    pass
                elif first_two % 2 == 0 or second_two % 2 == 0:
                    pass
                elif str(first_one) + str(first_two) == str(second_one) + str(second_two):
                    print(f"Cannot change the same player.")
                else:
                    count_changes += 1
                    if count_changes <= 6:
                        print(f"{first_one}{first_two} - {second_one}{second_two}")

                    else:
                        enough_changes = True
                        break
            if enough_changes:
                break

        if enough_changes:
            break

    if enough_changes:
        break
