l=[1,3,4,5,6,7,8,8,9,10]

l1=l[0::2]
l2=l[1::2]
if sum(l1)>sum(l2):
    print("Even sum is greater")
else:
    print("Odd sum is greater")