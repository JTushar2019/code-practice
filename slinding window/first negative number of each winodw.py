arr = [4, -5, 4, 3, -1, -9, -8, 5, 4, 7, 9, -3, -1, 4, -5, 8]

def foo(arr,k):
    list = []
    result = []
    i = 0
    for j in range(len(arr)):
        if arr[j] < 0:
            list.append(arr[j])
        if j-i+1 < k:
            continue
        else:
            if len(list) == 0:
                result.append(0)
            elif arr[i] == list[0]:
                result.append(list.pop(0))
            else:
                result.append(list[0])
            i += 1
    return result

print(foo(arr,1))





