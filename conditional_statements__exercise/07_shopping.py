budget = float(input())
video_card_qty = int(input())
processor_qty = int(input())
ram_qty = int(input())

video_card_price = 250
video_card_total = video_card_price * video_card_qty
processor_price = (video_card_total * .35) * processor_qty
ram_price = (video_card_total * .1) * ram_qty

total_cost = video_card_total + processor_price + ram_price

discount = 0
result = 0
diff = 0

if video_card_qty > processor_qty:
    discount = total_cost * .15
    result = total_cost - discount
    diff = budget - result

if budget >= total_cost:
    result = total_cost - discount
    diff = budget - result
    print(f"You have {diff:.2f} leva left!")
else:
    result = total_cost - discount
    diff = result - budget
    print(f"Not enough money! You need {diff:.2f} leva more!")
