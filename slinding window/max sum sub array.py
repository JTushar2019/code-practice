arr = [4, -5, 4, 3, -1, -9, -8, 5, 4, 7, 9, -3, -1, 4, -5, 8]

def foo(arr,k):
    i = 0
    sum = 0
    max_sum = 0
    for j in range(len(arr)):
        sum += arr[j]
        if j-i+1 < k:
            continue
        else:
            max_sum = max(max_sum, sum)
            sum -= arr[i]
            i += 1

    return max_sum

print(foo(arr,1))