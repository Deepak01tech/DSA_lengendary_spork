a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
def gcd(x, y):
    while x>0 and y>0:
        if x > y:
            x=  x%y
        else:
            y = y % x
    if x == 0:
        return y
    return x