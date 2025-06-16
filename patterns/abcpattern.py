"""
A
B B
C C C
D D D D 
"""
for i in range(5):
    for j in range(i):
        print(chr(64+i),end=" ")

    print()
