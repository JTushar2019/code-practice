a = [51, 32, 45, 1, 86, 42, 12, 32, 63, 20, 10, 94, 80, 75]
b = [15, 14, 3, 5]


def put(arr, n, last):
    if n == 0 or arr[n - 1] <= last:
        arr[n] = last
        return
    temp = arr[n - 1]
    put(arr, n - 1, last)
    arr[n] = temp


def foo(arr, n):
    if n == 1:
        return
    last = arr[n - 1]
    foo(arr, n - 1)
    put(arr, n - 1, last)


foo(a, len(a))
print(a)

print()
foo(b, len(b))
print(b)
