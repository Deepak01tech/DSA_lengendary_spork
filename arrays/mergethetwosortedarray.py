def merge(l1, l2):
    n=len(l1)
    m=len(l2)
    i=0
    j=0
    res=[]
    while i<n and j<m:
        if l1[i]<l2[j]:
            res.append(l1[i])
            i+=1
        else:       #l2[j]<=l1[i]
            res.append(l2[j])
            j+=1

    while i<n:
        res.append(l1[i])
        i+=1

    while j<m:
        res.append(l2[j])
        j+=1

    return res

l1=eval(input("Enter the first list : "))
l2=eval(input("Enter the second list : "))

print(merge(l1,l2))