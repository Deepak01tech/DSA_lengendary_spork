from typing import List
class Solution:
    def kidsWithCandies(self, l: List[int], ec: int) -> List[bool]:
        m=max(l)
        res=[]
        for i in range(0, len(l)):
            res.append(l[i]+ec>=m)
        return res

# Example usage:
l = [2, 3, 5, 1, 3]
ec = 3
solution = Solution()
result = solution.kidsWithCandies(l, ec)
print(result)  # Output: [True, True, True, False, True]
# The code defines a class Solution with a method kidsWithCandies that takes a list of integers and an integer as input and returns a list of booleans indicating whether each child can have the greatest number of candies after receiving extra candies. The method finds the maximum number of candies in the list and checks if each child's candies plus the extra candies are greater than or equal to the maximum.