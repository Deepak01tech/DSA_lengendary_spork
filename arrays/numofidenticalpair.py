from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    ans+=1
        return ans

# Example usage:
nums = [1, 2, 3, 1, 1, 3]
solution = Solution()
result = solution.numIdenticalPairs(nums)
print(result)  # Output: 4 (The pairs are: (0, 3), (0, 4), (3, 4), (2, 5))
# The code defines a class Solution with a method numIdenticalPairs that takes a list of integers as input and returns the number of good pairs in the list. A good pair is defined as a pair of indices (i, j) such that nums[i] == nums[j] and i < j.

'''
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        d={}
        for i in range(n):
            d[nums[i]]=0
        for i in range(n):
            d[nums[i]]=d[nums[i]]+1

        for count in d.values():
            ans+=(count*(count-1))//2

        return ans

'''