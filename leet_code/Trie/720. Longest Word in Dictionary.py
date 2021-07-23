# https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:

    def longestWord(self, words):
        adj_matrix = [[0] * 26]
        is_final = {0: True}
        vertex = 0
        for each in words:
            node = 0
            for c in each:
                t = ord(c) - ord('a')
                if adj_matrix[node][t] == 0:
                    vertex += 1
                    adj_matrix[node][t] = vertex
                    adj_matrix.append([0] * 26)
                node = adj_matrix[node][t]
            is_final[node] = True
            print(each[-1])
        for each in is_final.items():
            print(each)
        ans = ""
        current = []

        def dfs(node):
            nonlocal ans, current,adj_matrix,is_final
            if len(current) > len(ans):
                ans = "".join(current)

            for i in range(26):
                if adj_matrix[node][i] != 0 and adj_matrix[node][i] in is_final:
                    current.append(chr(ord('a') + i))
                    dfs(adj_matrix[node][i])
                    current.pop()

        dfs(0)
        return ans


    def foo(self, words):
        from collections import OrderedDict as dict
        d = dict.fromkeys(sorted(words))
        ans = ""
        # print(d.items())
        for each in d:
            t = each
            b = True
            while len(t) > 1:
                if t[:-1] not in d:
                    b = False
                    break
                t = t[:-1]
            if b and len(each) > len(ans):
                ans = each
        return ans






s = Solution()
# print(s.longestWord(["w","wo","wor","worl","world"]))
# print(s.longestWord(["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]))

print(s.foo(["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]))

print(s.foo(["a","banana","app","appl","ap","apply","apple"]))