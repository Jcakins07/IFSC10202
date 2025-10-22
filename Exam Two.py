properties = []

with open("Exam Two Properties.csv", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) < 5:
            continue
        parts[4] = float(parts[4])
        properties.append(parts)

print(f"{'Address':35} {'City':15} {'State':5} {'Zip':8} {'Price'}")
for p in properties:
    print(f"{p[0]:35} {p[1]:15} {p[2]:5} {p[3]:8} ${p[4]:,.2f}")

zipcodes = []
for p in properties:
    zip_code, price = p[3], p[4]
    for z in zipcodes:
        if z[0] == zip_code:
            z[1] += 1
            z[2] += price
            break
    else:
        zipcodes.append([zip_code, 1, price])

print("\n{:>10} {:>8} {:>15}".format("Zipcode", "Count", "Average"))
for z in zipcodes:
    avg = z[2] / z[1]
    print(f"{z[0]:>10} {z[1]:>8} {avg:>15,.2f}")
