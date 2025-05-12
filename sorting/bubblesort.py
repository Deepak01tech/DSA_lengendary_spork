n=eval((input("Enter the list: ")))
l=len(n)
def bubblesort(n):
    for i in range(l):
        for j in range(0,l-i-1):
            if n[j] > n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]
    return n
print(bubblesort(n))
