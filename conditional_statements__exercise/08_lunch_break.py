import math

tv_series = input()
episode_mins = int(input())
brake_mins = int(input())

lunch = brake_mins / 8
chill = brake_mins / 4

break_left = brake_mins - (lunch + chill)

diff = break_left - episode_mins
diff = math.ceil(diff)
diff2 = episode_mins - break_left
diff2 = math.ceil(diff2)

if episode_mins <= break_left:
    print(f"You have enough time to watch {tv_series} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {tv_series}, you need {diff2} more minutes.")
