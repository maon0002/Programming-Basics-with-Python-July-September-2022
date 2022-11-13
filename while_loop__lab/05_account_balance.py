deposit = ""
total_deposit = 0

while True:
    deposit = input()
    if deposit == "NoMoreMoney":
        break

    money = float(deposit)

    if money < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {money:.2f}")
        total_deposit += money

print(f"Total: {total_deposit:.2f}")
