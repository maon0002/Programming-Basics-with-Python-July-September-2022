n = int(input())

even_total = 0
odd_total = 0

for i in range(n):
    next_num = int(input())
    if i % 2 == 0:
        even_total += next_num
    else:
        odd_total += next_num

diff = abs(even_total - odd_total)

if even_total == odd_total:
    print(f"Yes")
    print(f"Sum = {even_total}")
else:
    print(f"No")
    print(f"Diff = {diff}")
