def linear_search(key, arr):
    for i in range(len(arr)):
        return i if arr[i] == key else None


def global_linear_search(key, arr):
    results = []
    for i in range(len(arr)):
        if arr[i] == key:
            results.append(i)

    if len(results) == 0:
        return None
    else:
        return results


print(linear_search(1, [1, 3, 5]))  # 0
bananas_list = ["b", "a", "n", "a", "n", "a", "s"]
print(global_linear_search("a", bananas_list))  # 1, 3, 5
print(global_linear_search(3, [1, 2, 3]))  # 2
print(global_linear_search(4, [1, 2, 3]))  # undefined
print(global_linear_search(13, [1, 2, 3]))  # undefined
