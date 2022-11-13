week_day = input()
week_day_status = ""

if week_day == "Monday" \
        or week_day == "Tuesday" \
        or week_day == "Wednesday" \
        or week_day == "Thursday" \
        or week_day == "Friday":
    week_day_status = "Working day"
elif week_day == "Saturday" \
        or week_day == "Sunday":
    week_day_status = "Weekend"
else:
    week_day_status = "Error"

print(week_day_status)
