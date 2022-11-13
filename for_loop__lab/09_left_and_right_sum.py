n = int(input())  # 2
first_nums_total = 0
second_nums_total = 0

for i in range(2 * n):
    next_num = int(input())
    if i < n:
        first_nums_total += next_num
    else:
        second_nums_total += next_num

diff = abs(first_nums_total - second_nums_total)

if first_nums_total == second_nums_total:
    print(f"Yes, sum = {second_nums_total}")
else:
    print(f"No, diff = {diff}")
