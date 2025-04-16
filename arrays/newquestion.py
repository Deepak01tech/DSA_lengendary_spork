def getMinimumAlterations(server_health):
    alterations = 0
    n = len(server_health)

    # We will iterate through the string and look for the patterns "010" and "101"
    i = 0
    while i < n - 2:
        # Check for the subsequence "010"
        if server_health[i:i+3] == "010":
            alterations += 1
            # To avoid overlapping issues, we can skip the next two characters
            i += 1
        # Check for the subsequence "101"
        elif server_health[i:i+3] == "101":
            alterations += 1
            # To avoid overlapping issues, we can skip the next two characters
            i += 1
        else:
            i += 1

    return alterations

print(getMinimumAlterations("001100"))