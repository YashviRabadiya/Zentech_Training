# A 
# B B 
# C C C 
# D D D D 
# E E E E E

n = int(input("Enter a number: "))
letter = 'A'

for i in range(n):
    for j in range(i + 1):

        print(letter, end=" ")

    letter = chr(ord(letter) + 1)
    print()