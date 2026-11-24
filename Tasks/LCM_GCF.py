a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

x = a
y = b

while y:
    x, y = y, x % y

gcf = x
lcm = (a * b) // gcf

print("GCF:", gcf)
print("LCM:", lcm)