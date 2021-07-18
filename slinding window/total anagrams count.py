a = "cbaebabacd"
b = "abc"


def findAnagrams(s: str, p: str):
    from collections import Counter as counter

    l = counter(p)
    k = len(p)
    count = len(l)
    result = []
    i = 0
    for j in range(len(s)):
        if s[j] in l:
            l[s[j]] -= 1

            if l[s[j]] == 0:
                count -= 1

        if j - i + 1 == k:
            if count == 0:
                result.append(i)

            if s[i] in l:
                if l[s[i]] == 0:
                    count += 1
                l[s[i]] += 1

            i += 1
    return result

print(findAnagrams(a, b))
