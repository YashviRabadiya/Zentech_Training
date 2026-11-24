# *       *
# **     **
# ***   ***
# **** ****
# *********

n = 5
for i in range(1,n):
    stars = '*'*(i)
    spaces = ' '*(2*(n-i)-1)
    print(stars+spaces+stars)

print('*'*(2*n-1))