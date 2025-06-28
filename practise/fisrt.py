# nums=[1, 2, 3, 4]

# l=[]

# for i in range(len(nums)):
#     s = 1
#     for j in range(len(nums)):
#         if j != i:
#             s *= nums[j]

#     l.append(s)

# print(l)

# implement polymorphism
# overloading
# function with same name but different parameters
def add(a, b):
    return a + b
def add(a, b, c):
    return a + b + c

# overriding
def add(a, b):
    return a + b
class Calculator:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c