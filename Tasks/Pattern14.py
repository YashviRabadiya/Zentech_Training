# 21 20 19 18 17 16 
# 15 14 13 12 11 
# 10 9 8 7 
# 6 5 4 
# 3 2 
# 1 

n = 6
num = (n*(n+1))//2
for i in range(n,0,-1):
    for j in range(i):
        print(num,end=' ')
        num -= 1
    print()