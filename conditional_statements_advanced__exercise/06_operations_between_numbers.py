first_num = int(input())
second_num = int(input())
operator = input()

number_type = ""
result = 0
is_zero = False

if operator == "+":  # or operator == "-" or operator == "*":
    result = first_num + second_num
elif operator == "-":
    result = first_num - second_num
elif operator == "*":
    result = first_num * second_num
elif operator == "/" and second_num != 0:
    result = first_num / second_num
elif operator == "%" and second_num != 0:
    result = first_num % second_num

even_or_odd = result % 2 == 0
if even_or_odd:
    even_or_odd = "even"
else:
    even_or_odd = "odd"

if operator == "+" \
        or operator == "-" \
        or operator == "*":
    print(f"{first_num} {operator} {second_num} = {result} - {even_or_odd}")
elif operator == "/":
    if second_num != 0:
        print(f"{first_num} / {second_num} = {result:.2f}")
    else:
        print(f"Cannot divide {first_num} by zero")
elif operator == "%":
    if second_num != 0:
        print(f"{first_num} % {second_num} = {result}")
    else:
        print(f"Cannot divide {first_num} by zero")
