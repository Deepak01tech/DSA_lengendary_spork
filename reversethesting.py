s="heello"
print(s[::-1])

rever=""
for i in s:
    rever=i+rever
print(rever)

for i in range(len(s)-1,-1,-1):
    print(s[i],end="")

print(2*s)
print(s*2)