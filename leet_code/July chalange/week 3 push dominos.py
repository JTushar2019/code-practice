# https://leetcode.com/problems/push-dominoes/
# https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3821/


def pushDominoes(dominoes):
    s = list(dominoes)
    # print(s)
    j = 0

    while j < len(s):
        if s[j] == '.':
            j += 1
        elif s[j] == 'L':
            k = j - 1
            while k >= 0 and s[k] == '.':
                s[k] = 'L'
                k -= 1
            j += 1
        else:
            k = j + 1
            while k < len(s) and s[k] == '.':
                s[k] = 'R'
                k += 1
            if k < len(s) and s[k] == 'L':
                count = k - j + 1
                for p in range(j + count // 2, k):
                    s[p] = 'L'
                if count % 2:
                    s[j + count // 2] = '.'
                j = k + 1
            else:
                j = k
    return "".join(s)


print(pushDominoes("RR.L"))
print(pushDominoes(".L.R...LR..L.."))