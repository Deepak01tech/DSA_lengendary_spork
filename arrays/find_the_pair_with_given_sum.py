def pair(l,sum):
    l.sort()
    i = 0
    j = len(l) - 1
    while i < j:
        if l[i] + l[j] == sum:
            return True
        elif l[i] + l[j] < sum:
            i += 1
        else:
            j -= 1
    return False

l=eval(input("Enter the array: "))
sum=int(input("Enter the sum: "))
print("The array is: ",l)
print("The sum is: ",sum)
if pair(l,sum):
    print("The pair with the given sum is present in the array.")
else:
    print("The pair with the given sum is not present in the array.")

