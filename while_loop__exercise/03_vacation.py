needed_money = float(input())
budget = float(input())
days_counter = 0
spend_days_counter = 0

while budget < needed_money and spend_days_counter < 5:
    action = input()
    action_sum = float(input())
    days_counter += 1
    if action == "save":
        budget += action_sum
        spend_days_counter = 0
    elif action == "spend":
        spend_days_counter += 1
        budget -= action_sum
        if budget < 0:
            budget = 0
    else:
        continue

if spend_days_counter == 5:
    print(f"You can't save the money.")
    print(f"{days_counter}")

if budget >= needed_money:
    print(f"You saved the money for {days_counter} days.")
