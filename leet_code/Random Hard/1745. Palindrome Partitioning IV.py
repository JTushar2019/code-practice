# https://leetcode.com/problems/palindrome-partitioning-iv/


class Solution:
    def checkPartitioning(self, s):
        from collections import defaultdict, deque
        l = len(s)
        n = 0
        arr = [0] * (l + 1)
        now = l - 2
        arr[-1] = 0
        arr[-2] = 1
        d = defaultdict(deque)
        d[s[-1]].append(l - 1)
        while now > -1:
            minimum = 1 + arr[now + 1]
            if minimum == 2 and now > 0 and hash(s[:now]) == hash(s[:now][::-1]):
                return True

            for end in d[s[now]]:
                temp = s[now:end + 1]
                if hash(temp) == hash(temp[::-1]):
                    minimum = min(minimum, 1 + arr[end + 1])
            arr[now] = minimum
            d[s[now]].append(now)
            now -= 1
        return arr[0] == 3

