result = map(int, ["1", "2", "3"])
print(list(result))  # Output: <map object at 0x...>
print(list(result))  # Output: [1, 2, 3]
print(list(filter(lambda x: x>0,result))) # Output: empty list because after one time use it get exhausted