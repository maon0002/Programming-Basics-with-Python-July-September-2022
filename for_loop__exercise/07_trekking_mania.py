groups_num = int(input())
group_1 = 0  # MUSALA
group_2 = 0  # MONBLANC
group_3 = 0  # KILIMANJARO
group_4 = 0  # K2
group_5 = 0  # EVEREST

top = ""

for group in range(groups_num):
    people_in_group = int(input())
    if people_in_group <= 5:
        group_1 += people_in_group
    elif 6 <= people_in_group <= 12:
        group_2 += people_in_group
    elif 13 <= people_in_group <= 25:
        group_3 += people_in_group
    elif 26 <= people_in_group <= 40:
        group_4 += people_in_group
    elif people_in_group >= 41:
        group_5 += people_in_group

total_people = group_1 + group_2 + group_3 + group_4 + group_5
print(f"{(group_1 / total_people) * 100:.2f}%")
print(f"{(group_2 / total_people) * 100:.2f}%")
print(f"{(group_3 / total_people) * 100:.2f}%")
print(f"{(group_4 / total_people) * 100:.2f}%")
print(f"{(group_5 / total_people) * 100:.2f}%")
