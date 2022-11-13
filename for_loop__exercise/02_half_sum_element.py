import sys

n = int(input())  # 7
max_n = -sys.maxsize
n_total = 0

for num in range(n):
    next_n = int(input())
    n_total += next_n
    if next_n > max_n:
        max_n = next_n

total = abs(n_total - max_n)
diff = abs(total - max_n)

if total == max_n:
    print(f"Yes")
    print(f"Sum = {max_n}")
else:
    print(f"No")
    print(f"Diff = {diff}")
