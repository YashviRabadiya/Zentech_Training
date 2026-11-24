# *       *       *
#  *     * *     * *
#   *   *   *   *   *
#    * *     * *     *
#     *       *       *

n = int(input("Enter a number: "))

for i in range(n):
    
    print(' '*i,end='')
    print('*',end='')
 
    print(' '*(2*(n-i)-3), end='')
    if i < n-1:
        print('*',end='')

    print(' '*(2*i-1),end='')
    if i > 0:
        print('*',end='')

    print(' '*(2*(n-i)-3), end='')
    if i < n-1:
        print('*',end='')

    print(' '*(2*i-1),end='')
    if i > 0:
        print('*')
    if i == 0:
        print()

# n = int(input("Enter the value of n: "))

# for i in range(n):
#     for j in range(5 * (n - 1) + 1):

#         if j == i or j == 2*(n-1)-i or j == 2*(n-1)+i or j == 4*(n-1)-i or j == 4*(n-1)+i:
#             print("*", end="")
#         else:
#             print(" ", end="")

#     print()