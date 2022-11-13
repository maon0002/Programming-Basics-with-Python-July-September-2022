period_range = int(input())

medics_start_count = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, period_range + 1):
    patients = int(input())
    if day % 3 != 0:
        if patients <= medics_start_count:
            treated_patients += patients
        else:
            untreated_patients += abs(patients - medics_start_count)
            treated_patients += medics_start_count
    else:
        if treated_patients < untreated_patients:
            medics_start_count += 1
            if patients <= medics_start_count:
                treated_patients += patients
            else:
                untreated_patients += abs(patients - medics_start_count)
                treated_patients += medics_start_count
        else:
            if patients <= medics_start_count:
                treated_patients += patients
            else:
                untreated_patients += abs(patients - medics_start_count)
                treated_patients += medics_start_count

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
