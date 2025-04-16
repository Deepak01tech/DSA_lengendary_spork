n=int(input("enter the number"))


l=list(range(1,n))

for i in range(0,n):
    print(f"Element at index {i} in list l is {l[i-1]}")
