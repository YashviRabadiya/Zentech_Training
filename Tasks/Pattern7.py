#         1 
#       2 3 2 
#     3 4 5 4 3 
#   4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5

n = int(input("Enter a number: "))

for i in range(n):

    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(i+1):
        print(j+i+1, end=" ")

    for j in range(i,0,-1):
        print(j+i, end=" ")
    print()