start_points = int(input())
bonus = ''

if start_points % 2 == 0:
    bonus = 1
elif start_points % 5 == 0:
    bonus = 2
else:
    bonus = 0

if start_points > 1000:
    print(start_points * 0.1 + bonus)
    print(start_points * 1.1 + bonus)
elif start_points > 100:
    print(start_points * 0.2 + bonus)
    print(start_points * 1.2 + bonus)
else:
    print(5 + bonus)
    print(start_points + 5 + bonus)
