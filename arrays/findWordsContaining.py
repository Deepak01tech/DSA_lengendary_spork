from typing import List
# The code defines a class Solution with a method findWordsContaining that takes a list of strings and a character as input and returns a list of indices of the strings that contain the specified character. The method iterates through the list of strings, checks if the character is present in each string, and appends the index to the result list if it is found.
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for i in range(0,len(words)):
            if x in words[i]:
                ans.append(i)
        return ans

# Example usage:
words = ["hello", "world", "python", "programming"]
x = "o"
solution = Solution()
result = solution.findWordsContaining(words, x)
print(result)  # Output: [0, 1] (Indices of words containing 'o')
