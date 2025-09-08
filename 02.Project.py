from math import pi, sin, cos, acos

print("Great Circle Calculator")
r = float(input("Enter Radius of Sphere: "))
x1 = float(input("Starting Point - Enter Latitude: ")) * pi / 180
y1 = float(input("Starting Point - Enter Longitude: ")) * pi / 180
x2 = float(input("Ending Point - Enter Latitude: ")) * pi / 180
y2 = float(input("Ending Point - Enter Longitude: ")) * pi / 180

d = r * acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))
print(f"The Great Circle Distance is {round(d, 2)}")
