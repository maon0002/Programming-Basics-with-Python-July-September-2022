pack_for_logistics = int(input())

microbus = 0
truck = 0
train = 0
microbus_rate = 0
truck_rate = 0
train_rate = 0
pack_weight_count = 0
microbus_tons_count = 0
truck_tons_count = 0
train_tons_count = 0

for pack in range(pack_for_logistics):
    pack_weight = int(input())
    if pack_weight <= 3:
        microbus += 1
        microbus_rate += (pack_weight * 200)
        pack_weight_count += pack_weight
        microbus_tons_count += pack_weight
    elif 4 <= pack_weight <= 11:
        truck += 1
        truck_rate += (pack_weight * 175)
        pack_weight_count += pack_weight
        truck_tons_count += pack_weight
    elif pack_weight >= 12:
        train += 1
        train_rate += (pack_weight * 120)
        pack_weight_count += pack_weight
        train_tons_count += pack_weight

total_logistics_count = microbus + truck + train
total_price = microbus_rate + truck_rate + train_rate
total_tons_count = microbus_tons_count + truck_tons_count + train_tons_count
avg_price = total_price / pack_weight_count

print(f"{avg_price:.2f}")
print(f"{(microbus_tons_count / total_tons_count) * 100:.2f}%")
print(f"{(truck_tons_count / total_tons_count) * 100:.2f}%")
print(f"{(train_tons_count / total_tons_count) * 100:.2f}%")
