month = input()  # May, June, July, August, September или October;
nights = int(input())

apartment = 0
studio = 0
studio_discount = 0
apartment_discount = 0

if month == "May" or month == "October":
    studio = 50.00
    apartment = 65.00
    if nights > 14:
        studio_discount = 0.30
        apartment_discount = 0.10
        studio = studio - (studio * studio_discount)
        apartment = apartment - (apartment * apartment_discount)
    elif nights > 7:
        studio_discount = 0.05
        studio = studio - (studio * studio_discount)
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        studio_discount = 0.20
        apartment_discount = 0.10
        studio = studio - (studio * studio_discount)
        apartment = apartment - (apartment * apartment_discount)
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if nights > 14:
        apartment_discount = 0.10
        apartment = apartment - (apartment * apartment_discount)

total_studio = studio * nights
total_apartment = apartment * nights

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
