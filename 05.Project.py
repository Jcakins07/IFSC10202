def is_special(n):
    x, digits, total = n, 0, 0
    while x > 0:
        x //= 10
        digits += 1
    x = n
    while x > 0:
        total += (x % 10) ** digits
        x //= 10
    return total == n

start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))

print(f"\nSpecial Numbers between {start} and {end}")
for i in range(start, end + 1):
    if is_special(i):
        print(i)
