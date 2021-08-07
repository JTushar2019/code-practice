# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3872/

class Solution:

    def minCut(self, s):
        from collections import defaultdict, deque
        data = defaultdict(deque)

        l = len(s)
        for i in range(l):
            data[s[i]].appendleft(i)
        anstable = {}

        def utility(start):
            nonlocal data, l, s
            temp = 2000
            if start == l:
                return 0
            if start == l - 1:
                return 1
            if start in anstable:
                return anstable[start]

            for i in data[s[start]]:
                if i < start:
                    break
                if start == i or hash(s[start:i + 1]) == hash(s[start:i + 1][::-1]):
                    temp = min(temp, utility(i + 1) + 1)
            anstable[start] = temp
            return temp

        t = utility(0) - 1
        print(t)
        return t


s = Solution()
# s.minCut("aaba")
# s.minCut("aabal")
# s.minCut("labaa")
# s.minCut("a")
# s.minCut("ab")
# s.minCut(
#     "adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"
#     )
