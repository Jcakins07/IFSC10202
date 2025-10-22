import csv

with open("09.Project Distances.csv") as f:
    table = list(csv.reader(f))

print("\nDistance Table:\n")
for row in table:
    print("".join(f"{item:>10}" for item in row))

from_city = input("\nEnter From City: ").strip()
to_city = input("Enter To City: ").strip()

row_index = next((i for i, row in enumerate(table) if row[0].lower() == from_city.lower()), None)
col_index = next((i for i, city in enumerate(table[0]) if city.lower() == to_city.lower()), None)

if row_index is None:
    print("Invalid From City")
elif col_index is None:
    print("Invalid To City")
else:
    print(f"\n{from_city} to {to_city} - {table[row_index][col_index]} miles")
