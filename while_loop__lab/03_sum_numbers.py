initial_num = int(input())
next_nums_sum = 0

while True:
    if next_nums_sum < initial_num:
        next_num = int(input())
        next_nums_sum += next_num
    else:
        print(next_nums_sum)
        break
