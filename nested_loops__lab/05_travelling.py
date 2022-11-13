destination = input()

saved_money = 0

while destination != "End":
    budget = float(input())
    while saved_money < budget:
        cash_in = float(input())
        saved_money += cash_in

        if saved_money >= budget:
            print(f"Going to {destination}!")
            saved_money = 0
            destination = input()
            break
