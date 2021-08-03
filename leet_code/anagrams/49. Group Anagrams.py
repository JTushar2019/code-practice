# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        l = len(strs)
        tempstr = defaultdict(list)
        for i in range(l):
            t = sorted(strs[i])
            tempstr[t].append(strs[i])
        return tempstr.values()