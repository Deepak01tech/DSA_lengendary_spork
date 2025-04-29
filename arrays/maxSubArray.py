from typing import List
# The code defines a class Solution with a method maxSubArray that takes a list of integers as input and returns the maximum sum of a contiguous subarray. The method uses Kadane's algorithm to find the maximum sum efficiently in O(n) time complexity. It initializes a variable to keep track of the current sum and updates the maximum sum found so far. If the current sum becomes negative, it resets it to zero.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        m=-100001
        cs=0
        for i in range(n):
            cs+=nums[i]
            m=max(m,cs)
            if cs<0:
                cs=0
        return m

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
result = solution.maxSubArray(nums)
print(result)  # Output: 6 (The contiguous subarray [4, -1, 2, 1] has the largest sum = 6)