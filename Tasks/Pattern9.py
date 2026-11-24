#         1   
#       1   1   
#     1   2   1   
#   1   3   3   1   
# 1   4   6   4   1 

n = int(input("Enter a number: "))

for i in range(1, n+1):
    temp = 1
    
    for j in range(1,n-i+1):
        print(" ", end=" ")

    print(temp, end="   ")

    for j in range(1,i):
        temp = (temp*(i-j))//j
        print(temp, end="   ")
    print()