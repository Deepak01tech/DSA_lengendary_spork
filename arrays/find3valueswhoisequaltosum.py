def sumof_3values(nums, sum):
    nums.sort()
    n=len(nums)

    for i in range(0,n-2):
        j=i+1
        k=n-1
        while j<k:
            if nums[i]+nums[j]+nums[k]==sum:
                return "Yes found"
            elif nums[i]+nums[j]+nums[k]>sum:
                k-=1
            else:
                j+=1
    return "Not found"


l=eval(input("Enter the list : "))
sum=int(input("Enter the desired sum : "))

print(sumof_3values(l,sum))