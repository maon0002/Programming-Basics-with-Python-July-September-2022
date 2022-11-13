import sys

n = int(input())

min_number = sys.maxsize
max_number = -sys.maxsize

for x in range(n):
    next_num = int(input())
    if next_num < min_number:
        min_number = next_num
    if next_num > max_number:
        max_number = next_num

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
