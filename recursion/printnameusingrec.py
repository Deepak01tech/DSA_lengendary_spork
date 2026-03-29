
# name = input("Enter your name: ")
def print_name(n, index=0):
    if index < len(n):
        print(n[index])
        print_name(n, index + 1)
# print_name(name)

# Example usage:
# Enter your name: Alice
# Output:

def print_1_to_N(n):
    if n == 0:
        return
    print(n, end=' ')
    print_1_to_N(n - 1)
    # print(n, end=' ')
print_1_to_N(5)  # Output: 1 2 3 4 5dee