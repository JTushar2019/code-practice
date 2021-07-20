# https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

arr = [4, 5, 5, -5, 0, 0, 3]
# here the window size is variable.

def largest_subarray_sum(arr, k):
    # when all are positive number then this can work
    result = 0
    i = 0
    temp = 0

    for j in range(len(arr)):
        temp += arr[j]

        while temp > k:
            temp -= arr[i]
            i += 1

        if temp == k:
            result = max(result, j - i + 1)

    return result


print(largest_subarray_sum(arr, 5))


def largest_subarray_with_negative_number(arr, k):
    # this works in all the cases
    # it is important to retain the old index for any current temp
    # as we seek the longest. hence the least value for any temp is the best
    # hence dictionary is not updated if sum key already exist
    result = 0
    d = {}
    temp = 0
    for i in range(len(arr)):
        temp += arr[i]
        if temp == k:
            result = i + 1

        elif temp - k in d:
            result = max(result, i - d[temp - k])

        if temp not in d:
            d[temp] = i

    return result


print(largest_subarray_with_negative_number(arr, 5))