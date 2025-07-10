import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

count = 0
# To fix this, we can declare 'i' as global inside the function.
def PrintallSubsequence(s, i, curr):
    global count
    count+=1
    if i == len(s):
        print(count)
        print(curr)
        return

    # Include the current character
    PrintallSubsequence(s, i + 1, curr + s[i])

    # Exclude the current character
    PrintallSubsequence(s, i + 1, curr)

# Example usage
s = "abc"
PrintallSubsequence(s, 0, "")
# This will print all subsequences of the string "abc"
# Output:
# abc