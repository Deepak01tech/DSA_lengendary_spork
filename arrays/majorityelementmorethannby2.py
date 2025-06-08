# n=list(map(int, input("Enter the number of elements in the array: ").split()))
l= [2,2,1,1,1,2,2]
n=len(l)
d={}
for i in range(n):
    # d[l[i]]= d.get(l[i],0)+1
    if l[i] in d:
        d[l[i]]+=1
    else:
        d[l[i]]=1
for k,v in d.items():
    if v>n//2:
        print(k)


