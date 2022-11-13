import sys

expected_nums = int(input())

odd_total = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_total = 0
even_min = sys.maxsize
even_max = -sys.maxsize
odd_count = 0
even_count = 0

for position in range(1, expected_nums + 1):
    num = float(input())
    if position % 2 != 0:
        odd_total += num
        odd_count += 1
        if num < odd_min:
            odd_min = num
        if num > odd_max:
            odd_max = num
    elif position % 2 == 0:
        even_total += num
        even_count += 1
        if num < even_min:
            even_min = num
        if num > even_max:
            even_max = num

if odd_count == 0:
    odd_min = "No"
    odd_max = "No"
    print(f"OddSum={odd_total:.2f},")  # + {сума на числата на нечетни позиции},
    print(f"OddMin={odd_min},")  # + { минимална стойност на числата на нечетни позиции } / {“No”},
    print(f"OddMax={odd_max},")  # + { максимална стойност на числата на нечетни позиции } / {“No”},
else:
    print(f"OddSum={odd_total:.2f},")  # + {сума на числата на нечетни позиции},
    print(f"OddMin={odd_min:.2f},")  # + { минимална стойност на числата на нечетни позиции } / {“No”},
    print(f"OddMax={odd_max:.2f},")  # + { максимална стойност на числата на нечетни позиции } / {“No”},

if even_count == 0:
    even_max = "No"
    even_min = "No"
    print(f"EvenSum={even_total:.2f},")  # + { сума на числата на четни позиции },
    print(f"EvenMin={even_min},")  # + { минимална стойност на числата на четни позиции } / {“No”},
    print(f"EvenMax={even_max}")  # + { максимална стойност на числата на четни позиции } / {“No”}
else:
    print(f"EvenSum={even_total:.2f},")  # + { сума на числата на четни позиции },
    print(f"EvenMin={even_min:.2f},")  # + { минимална стойност на числата на четни позиции } / {“No”},
    print(f"EvenMax={even_max:.2f}")  # + { максимална стойност на числата на четни позиции } / {“No”}
