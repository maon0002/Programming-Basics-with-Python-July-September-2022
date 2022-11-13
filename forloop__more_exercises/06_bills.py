months = int(input())
water_per_month = 20
net_per_month = 15
electricity_total = 0
others = 0

for _ in range(months):
    electricity_bill = float(input())
    electricity_total += electricity_bill
    others += ((electricity_bill + water_per_month + net_per_month) * 1.20)

water_total = water_per_month * months
net_total = net_per_month * months
others_total = others

bills_total = electricity_total + water_total + net_total + others_total
avg = bills_total / months

print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water_total:.2f} lv")
print(f"Internet: {net_total:.2f} lv")
print(f"Other: {others_total:.2f} lv")
print(f"Average: {avg:.2f} lv")
