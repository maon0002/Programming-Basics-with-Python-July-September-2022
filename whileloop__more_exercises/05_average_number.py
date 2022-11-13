n = int(input())

sum_n = 0
count_n = 0

while count_n < n:
    input_num = int(input())
    sum_n += input_num
    count_n += 1

median = sum_n / count_n
print(f"{median:.2f}")
