def fun(n):
    if n == 0:
        return
    fun(n-1)
    print(n, end=' ')

fun(3)
# Output: 1 2 3 