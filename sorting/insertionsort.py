n=list(map(int, input("enter the list: ").split()))
l=len(n)
def insertionsort(n):
    for i in range(1,l):
        key=n[i]
        j=i-1
        while j>=0 and key<n[j]:
            n[j+1]=n[j]
            j-=1
        n[j+1]=key
    return n
print(insertionsort(n)) #4 6 7 8 5 43
print(*insertionsort(n)) #4 6 7 8 5 43