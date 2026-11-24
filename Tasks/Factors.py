# num = int(input("Enter a number to find its factors: "))

# for i in range(1, num//2 + 1):
#     if num % i == 0:
#         print(i)

num = int(input("Enter a number to find its factors: "))

for i in range(1, int(num ** 0.5) + 1):
    if num % i == 0:
        print(i)

        if i != num // i:
            print(num // i)