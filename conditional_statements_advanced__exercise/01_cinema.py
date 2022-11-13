screening_type = input()
rows = int(input())
columns = int(input())

seats = rows * columns

sales_value = 0

if screening_type == "Premiere":
    sales_value = seats * 12.00
elif screening_type == "Normal":
    sales_value = seats * 7.50
elif screening_type == "Discount":
    sales_value = seats * 5.00

print(f"{sales_value:.2f} leva")
