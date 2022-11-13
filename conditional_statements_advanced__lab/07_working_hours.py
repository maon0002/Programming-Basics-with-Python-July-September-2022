hour = int(input())
week_day = input()
office_status = ""

if 10 <= hour <= 18:
    if week_day == "Monday" \
            or week_day == "Tuesday" \
            or week_day == "Wednesday" \
            or week_day == "Thursday" \
            or week_day == "Friday" \
            or week_day == "Saturday":
        office_status = "open"
    else:
        office_status = "closed"

else:
    office_status = "closed"

print(office_status)
