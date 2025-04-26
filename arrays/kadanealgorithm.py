import sys
int_max = sys.maxsize
int_min = -sys.maxsize - 1

n= int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))

def kadane_algorithm(arr,n):
    maxi= int_min
    sum=0
    for i in range(n):
        sum+=arr[i]
        maxi=max(maxi,sum)
        if sum >maxi:
            maxi=sum
        if sum<0:
            sum=0
    return maxi

print("Maximum sum of subarray is: ", kadane_algorithm(arr,n))
print("time complexity is O(n)")
print("space complexity is O(1)")

