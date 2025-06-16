l = [2, 2, 1, 1, 1, 2, 2]
n = len(l)
count = 0
el = None

# Phase 1: Find candidate
for i in range(n):
    if count == 0:
        el = l[i]
        count = 1  # ✅ Fix: set count to 1
    elif l[i] == el:
        count += 1
    else:
        count -= 1

# Phase 2: Confirm candidate
count2 = 0
for i in range(n):
    if l[i] == el:
        count2 += 1

if count2 > n // 2:
    print(el)
