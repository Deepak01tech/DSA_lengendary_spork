from functools import reduce
n=123454566

s=str(n)
l=list(map(int,s))
print(max(l))
# print(reduce(sum,l))
