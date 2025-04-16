def merge(l1,l2):
    i=0
    j=0
    l3=[]
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            l3.append(l1[i])
            i+=1
        else:
            l3.append(l2[j])
            j+=1
    while i<len(l1):
        l3.append(l1[i])
        i+=1
    while j<len(l2):
        l3.append(l2[j])
        j+=1
    return l3
# l1=[1,3,5,7,9]
# l2=[2,4,6,8,10]
l1=eval(input("Enter the first sorted array: "))
l2=eval(input("Enter the second sorted array: "))
print("The first sorted array is: ",l1)
print("The second sorted array is: ",l2)
print("The merged sorted array is: ",merge(l1,l2))
