#Linear Search
l=eval(input("Enter the list : "))
ele=int(input("Enter the element : "))
for i in l:
    if i==ele:
        print("Yes")
        break
else:
    print("No")