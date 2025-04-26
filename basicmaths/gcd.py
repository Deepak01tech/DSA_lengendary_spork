n=int(input("enter the no : "))
m=int(input("enter the no : "))


def gcd(n,m):
    if m==0:
        return n
    else:
        return gcd(m,n%m)

print("gcd of ",n," and ",m," form recursive way  is ",gcd(n,m))

def gcd_iter(n,m):
    while m!=0:
        n,m=m,n%m
    return n
print("gcd of ",n," and ",m," form iterative way  is ",gcd_iter(n,m))

def gcd_euclidbyloop(n,m):
    while a>0 and b>0:
        if a>b:
            a=a%b
        else:
            b=b%a

    if n==0:
        return m
    else:
        return a