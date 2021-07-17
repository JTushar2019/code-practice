s = [45, 51,56,65,95]


def put(s, temp):
    if (len(s) == 0 or s[0] <= temp):
        s.insert(0, temp)
        return
    t = s.pop(0)
    put(s, temp)
    s.insert(0, t)


def sorting(s):
    if (len(s) == 1):
        return
    temp = s.pop(0)
    sorting(s)
    put(s, temp)


sorting(s)
print(s)

#jflalkfn
