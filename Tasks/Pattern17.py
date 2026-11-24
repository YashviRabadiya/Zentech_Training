# *********
# **** ****
# ***   ***
# **     **
# *       *

n = 5

print('*'*(2*n-1))

for i in range(n,1,-1):
    stars = '*'*(i-1)
    spaces = ' '*(2*(n-i)+1)
    print(stars+spaces+stars)