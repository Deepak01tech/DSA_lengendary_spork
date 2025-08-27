
def fibonaci(n):
    memo = [-1]*(n+1)
    memo[0] = 0
    memo[1] = 1


    def helper(n):
        if n not in memo:
            memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]

    return helper(n)

# Example usage:
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci of {n} is:", fibonaci(n))
