from math import floor

cup_nums = int(input())
start_points = int(input())

cup_points = 0

wins_count = 0

for cup in range(cup_nums):
    stage = input()
    if stage == "W":
        cup_points += 2000
        wins_count += 1
    elif stage == "F":
        cup_points += 1200
    elif stage == "SF":
        cup_points += 720

# The average of a set of numbers is simply the sum of the numbers divided by the total number of values in the set.
avg_points = floor(cup_points / cup_nums)  # колко точки средно печели от всички изиграни турнири
perc_wins = (wins_count / cup_nums) * 100  # колко процента от турнирите е спечелил
total_points = cup_points + start_points

print(f"Final points: {total_points}")
print(f"Average points: {avg_points}")
print(f"{perc_wins:.2f}%")
