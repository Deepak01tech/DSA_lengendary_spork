from collections import Counter
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

cou= Counter(nums)
print(cou)

t="a auick silver fox jumps over the lazy dog"
c=Counter(t)
print(c)
print(c.most_common(2))