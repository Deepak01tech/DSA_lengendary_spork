try:
    n=int(input("Enter the number:"))
    if n<0:
        raise ValueError("Number is negative")
    else:
        print("Number is positive")
# except ValueError as e:
#     print(e)