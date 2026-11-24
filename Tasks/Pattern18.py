# *******
# *** ***
# **   **
# *     *
# **   **
# *** ***
# *******

n = 4

print('*'*(2*n-1))

for i in range(n,1,-1):
    stars = '*'*(i-1)
    spaces = ' '*(2*(n-i)+1)
    print(stars+spaces+stars)

for i in range(2,n):
    stars = '*'*(i)
    spaces = ' '*(2*(n-i)-1)
    print(stars+spaces+stars)

print('*'*(2*n-1))