s = "abd"

result = ""


def foo(s, i, size, result):
    if i == size:
        print(result)
        return
    result += s[i]
    foo(s, i + 1, size, result)
    result = result[:-1]

    foo(s, i + 1, size, result)


foo(s, 0, len(s), "")
print()

def foo(s, r):
    if not len(s):
        print(r)
        return
    foo(s[1:], r)
    foo(s[1:], r + s[0])

foo(s,"")