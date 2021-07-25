# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7#problem

from random import shuffle as sf
from random import randint


def foo(size, req_sum):
    arr = list(range(1, size + 1))
    l = len(arr)
    found = False
    ans = []

    def recursive(i, cost):
        nonlocal arr, l, found
        if cost < 0:
            return

        if i == l - 1:
            if cost == 0:
                found = True
                ans = arr[:]
                reversort(ans)
            return
        for p in range(i, l):
            arr[i:p + 1] = arr[i:p + 1][::-1]
            recursive(i + 1, cost - (p - i + 1))
            arr[i:p + 1] = arr[i:p + 1][::-1]

    recursive(0, req_sum)

    if found:
        print(ans)
        return ans
    else:
        print("IMPOSSIBLE")
        return None


def reversort(arr):
    ans = 0
    for i in range(len(arr) - 1):
        # print(list(enumerate(arr)))
        index = arr.index(min(arr[i:]))
        # print(index)
        arr[i:index + 1] = arr[i:index + 1][::-1]
        ans += index - i + 1
        # print(arr)
    print(ans)
    return ans


# def test(n):
#     arr = list(range(1, n + 1))
#     sf(arr)
#     c = reversort(arr)
#     print(arr,c)
#     none_list = foo(n, c)
#     if none_list:
#         reversort(none_list)

foo(4,6)
# foo(2,2)
# foo(7, 12)
# foo(2, 1)

# test(2)
# test(9)
# test(5)
# test(9)