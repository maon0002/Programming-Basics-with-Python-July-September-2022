expected_charity = int(input())
cash_count = 0
card_count = 0
cash_sum = 0
card_sum = 0
sold_sum = 0
all_count = 0
goal = False
input_line = input()

while input_line != "End":
    price = int(input_line)
    all_count += 1
    if all_count % 2 != 0:
        if price <= 100:
            cash_count += 1
            sold_sum += price
            cash_sum += price
            print(f"Product sold!")
        else:
            print("Error in transaction!")
    else:
        if price >= 10:
            card_count += 1
            sold_sum += price
            card_sum += price
            print(f"Product sold!")
        else:
            print("Error in transaction!")

    if sold_sum >= expected_charity:
        goal = True
        break

    input_line = input()

if goal:
    avg_cash = cash_sum / cash_count
    avg_card = card_sum / card_count

    print(f"Average CS: {avg_cash:.2f}")
    print(f"Average CC: {avg_card:.2f}")

if input_line == "End":
    print(f"Failed to collect required money for charity.")
