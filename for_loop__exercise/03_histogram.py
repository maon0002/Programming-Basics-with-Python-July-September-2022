n = int(input())

count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

for num in range(n):
    num_next = int(input())
    if num_next < 200:
        count_p1 += 1
    elif 200 <= num_next <= 399:
        count_p2 += 1
    elif 400 <= num_next <= 599:
        count_p3 += 1
    elif 600 <= num_next <= 799:
        count_p4 += 1
    elif num_next >= 800:
        count_p5 += 1

percent_1 = count_p1 / n * 100
percent_2 = count_p2 / n * 100
percent_3 = count_p3 / n * 100
percent_4 = count_p4 / n * 100
percent_5 = count_p5 / n * 100

print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")
print(f"{percent_5:.2f}%")
