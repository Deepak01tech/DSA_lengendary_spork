n=[10,20,30,4,0,0,4,0,50,2,]
m=len(n)
count=0
for i in range(m):
    if n[i]==0:
        n[count],n[i] = n[i],n[count]
        count+=1
print(n)

l=[]