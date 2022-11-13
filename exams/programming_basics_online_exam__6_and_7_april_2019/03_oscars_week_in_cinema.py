movie = input()
hall_type = input()
sold_tickets = int(input())

price_ticket = 0

if hall_type == "normal":
    if movie == "A Star Is Born":
        price_ticket = 7.50
    elif movie == "Bohemian Rhapsody":
        price_ticket = 7.35
    elif movie == "Green Book":
        price_ticket = 8.15
    elif movie == "The Favourite":
        price_ticket = 8.75
elif hall_type == "luxury":
    if movie == "A Star Is Born":
        price_ticket = 10.50
    elif movie == "Bohemian Rhapsody":
        price_ticket = 9.45
    elif movie == "Green Book":
        price_ticket = 10.25
    elif movie == "The Favourite":
        price_ticket = 11.55
elif hall_type == "ultra luxury":
    if movie == "A Star Is Born":
        price_ticket = 13.50
    elif movie == "Bohemian Rhapsody":
        price_ticket = 12.75
    elif movie == "Green Book":
        price_ticket = 13.25
    elif movie == "The Favourite":
        price_ticket = 13.95

profit = price_ticket * sold_tickets

print(f"{movie} -> {profit:.2f} lv.")
