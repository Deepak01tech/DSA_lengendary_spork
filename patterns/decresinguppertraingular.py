
'''
1 2 3 4
5 6 7
8 9
10
'''
count=1
for i in range(1,6):
    for j in range(6-i,1,-1):
        print(count,end=" ")
        count+=1
    print()
