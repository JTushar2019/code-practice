# arr = [4, -5, 4, 3, -1, -9, -8, 5, 4, 7, 9, -3, -1, 4, -5, 8]
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]

from collections import deque


def max_of_subarrays(arr, n, k):
    list = deque()
    result = []
    i = 0
    for j in range(n):
        while len(list) and list[-1] < arr[j]:
            list.pop()

        list.append(arr[j])

        if j - i + 1 < k:
            continue
        else:
            result.append(list[0])
            if arr[i] == list[0]:
                list.popleft()
            i += 1
    return result


print(max_of_subarrays(arr, len(arr), 3))
