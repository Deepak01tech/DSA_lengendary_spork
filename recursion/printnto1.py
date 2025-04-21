def fun(n):

    if n == 0:
        return

    print(n, end=' ')
    fun(n-1)
fun(3)
# Output: 3 2 1
# The function prints numbers from n to 1 in decreasing order.