# https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1#

arr = [4, -5, 4, 3, -1, -9, -8, 5, 4, 7, 9, -3, -1, 4, -5, 8]


def printFirstNegativeInteger(arr, n, k):
    from collections import deque
    l = deque()
    result = []
    i = 0
    for j in range(n):
        if arr[j] < 0:
            l.append(arr[j])
        if j - i + 1 == k:
            if len(l) == 0:
                result.append(0)
            else:
                result.append(l[0])
                if arr[i] == l[0]:
                    l.popleft()
            i += 1
    return result


print(printFirstNegativeInteger(arr, len(arr), 3))