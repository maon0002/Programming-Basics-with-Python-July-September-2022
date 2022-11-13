import math

record = float(input())
distance = float(input())
meters_per_second = float(input())

# important notice on floor F - be careful wher you put it
water_resistance = math.floor(
    distance / 15) * 12.5  # съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.

personal_time = (distance * meters_per_second) + water_resistance

if personal_time < record:
    print(f" Yes, he succeeded! The new world record is {personal_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {personal_time - record:.2f} seconds slower.")
