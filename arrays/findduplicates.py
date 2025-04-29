from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq=[0]*(n+1)
        res=[]

        for i in range(n):
            freq[nums[i]]+=1

        for i in range(len(freq)):
            if freq[i]==2:
                res.append(i)
        return res

# Example usage:
nums = [4, 3, 2, 7, 8, 2, 3, 1]
solution = Solution()
result = solution.findDuplicates(nums)
print(result)  # Output: [2, 3]
# The code defines a class Solution with a method findDuplicates that takes a list of integers as input and returns a list of integers that appear twice in the input list. The method uses a frequency array to count the occurrences of each integer and then collects the integers that appear exactly twice into the result list.

'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        nums.append(n+1)
        for i in range(n):
            val=abs(nums[i])
            if nums[val]>0:
                nums[val]*=(-1)
            else:
                res.append(val)

        return res

'''