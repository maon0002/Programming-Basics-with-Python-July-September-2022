money_in_her_pocket = float(input())  # per day
profit_per_day = float(input())
expenses_total = float(input())
gift_price = float(input())

days_till_bday = 5
total_profit = profit_per_day * days_till_bday
total_money_in_her_pocket = money_in_her_pocket * days_till_bday
plus_total = total_profit + total_money_in_her_pocket
balance = plus_total - expenses_total

if balance >= gift_price:
    print(f"Profit: {balance:.2f} BGN, the gift has been purchased.")
else:
    diff = abs(balance - gift_price)
    print(f"Insufficient money: {diff:.2f} BGN.")
