tar=int(input("Enter the target : "))
l=0
r=tar
ans=0
while l<=r:
    mid=(l+r)//2
    if mid*mid<=tar:
        ans=mid
        l=mid+1

    else:
        r=mid-1


print(ans)

'''
Largest x such x^2<=tar:

tar=int(input("Enter the target : "))
l=0
r=tar
ans=0
while l<=r:
    mid=(l+r)//2
    if mid*mid<=tar:
        ans=mid
        l=mid+1
    else:
        r=mid-1

print(ans)

'''