n=eval(input("Enter the list: "))
l=len(n)
def selectionsort(n):
    for i in range(l):
        min_index = i
        for j in range(i+1, l):
            if n[j] < n[min_index]:
                min_index = j
        n[i], n[min_index] = n[min_index], n[i]
    return n