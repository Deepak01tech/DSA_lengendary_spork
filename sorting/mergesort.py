n = list(map(int, input("enter the list: ").split()))

def mergesort(n, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergesort(n, low, mid)
    mergesort(n, mid + 1, high)
    merge(n, low, mid, high)

def merge(arr, low, mid, high):
    left = list(arr[low:mid+1])
    right = list(arr[mid+1:high+1])
    i = 0
    j = 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

mergesort(n, 0, len(n) - 1)
print(n)
