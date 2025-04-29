def func(nums, sum):
    nums.sort()
    n=len(nums)
    i=0
    j=n-1
    print(nums)
    while i<j:
        print(nums[i],nums[j])
        if nums[i]+nums[j]>sum:
            j-=1
        elif nums[i]+nums[j]<sum:
            i+=1
        else:
            return True
    return False


l=eval(input("Enter the list : "))
sum=int(input("Enter the desired sum : "))

if func(l,sum):
    print("Yes found")
else:
    print("Not found")