l=[10,10,20,30,30,40,50,50,60,70,80,80,90]
res=1
for i in range(1,len(l)-1):
    if l[i]==l[res-1]:
        continue
    else:
        l[res]=l[i]
        res+=1
print(l[:res])
