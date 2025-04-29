s=input(" Enter the string : ")
l=0
r=len(s)-1
ans=-1
while l<=r:
    mid=(l+r)//2
    if s[mid]=="F":
        r=mid-1
    else:
        l=mid+1
        ans=mid
print(ans)