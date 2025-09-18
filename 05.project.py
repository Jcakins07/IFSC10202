def s(n):
    t, d = n, 0
    while t:
        t //= 10
        d += 1
    t, x = n, 0
    while t:
        x += (t % 10) ** d
        t //= 10
    return x == n

a = int(input("Enter Start of Range: "))
b = int(input("Enter End of Range: "))

print("Special Numbers between", a, "and", b)
for i in range(a, b + 1):
    if s(i):
        print(i)
