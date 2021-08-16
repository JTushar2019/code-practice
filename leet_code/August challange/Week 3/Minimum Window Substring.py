# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3891/


class Solution:
    def minWindow(self, s, t):
        from collections import Counter
        len1 = len(s)
        answer = len1 + 1
        script = ""
        tchar = set(t)
        c = Counter(t)

        i = 0
        while i < len1:
            if s[i] in tchar:
                break
            else:
                i += 1
        if i == len1:
            return ""

        j = i
        remain = len(c)
        while j < len1:
            if s[j] in tchar:
                c[s[j]] -= 1
                if c[s[j]] == 0:
                    remain -= 1
            else:
                j += 1
                continue

            while True:
                if s[i] in tchar and c[s[i]] < 0:
                    c[s[i]] += 1
                    if c[s[i]] == 1:
                        remain += 1
                    i += 1
                elif s[i] not in tchar:
                    i += 1
                else:
                    break

            if not remain and j - i + 1 < answer:
                script = s[i:j + 1]
                answer = j - i + 1

            j += 1

        print(script)
        return script

s = Solution()
s.minWindow(s="ADOBECODEBANC", t="ABC")
s.minWindow(s="a", t="a")
s.minWindow(s="a", t="aa")
s.minWindow("ndkjasfsjaagfacbaglbskchbskcbyabcjab", "jbn")
