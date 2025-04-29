
tar=int(input("Enter the target : "))
l=0
r=tar
ans=0
while l<=r:
    mid=(l+r)//2
    if mid*mid>=tar:
        ans=mid
        r=mid-1
    else:
        l=mid+1

print(ans)


'''
Find smallest x*x>=tar
```
tar=int(input("Enter the target : "))
l=0
r=tar
ans=0
while l<=r:
    mid=(l+r)//2
    if mid*mid>=tar:
        ans=mid
        r=mid-1
    else:
        l=mid+1

print(ans)
```

'''