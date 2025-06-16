
for i in range(1,6):
    for j in range(1,i):
        print(j,end=" ")
    print()
count=1
for i in range(1,6):
    for j in range(1,i):
        print(count,end=" ")
        count+=1
    print()
"""
1
1 2
1 2 3
1 2 3 4

1
2 3
4 5 6
7 8 9 10
"""
