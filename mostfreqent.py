l=[1,1,1,2,2,2,2,2,7,3,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,]

dic={}

for i in l:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)

maxfre=max(dic.values())
print(maxfre)
for key,values in dic.items():
    if values==maxfre:
        print(key)

from collections import Counter
c=Counter(l)
print(c)
print(" ".join(c.most_common(1)))