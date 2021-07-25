# https://leetcode.com/problems/word-ladder/
class Solution:

    def neighbour(self, s1, s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count > 1:
                    return False
        if count == 1:
            return True

    def ladderLength(self, beginWord, endWord, wordList):
        if beginWord not in wordList:
            wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        beginWord, endWord = endWord, beginWord
        vertex = dict.fromkeys(wordList)
        size = len(endWord)
        import math
        from collections import defaultdict, deque
        deapth = {node: math.inf for node in vertex}
        minlen = math.inf
        q = deque()
        q.append(beginWord)
        deapth[beginWord] = 0
        visisted = defaultdict(bool)

        while len(q):
            node = q.popleft()
            vertex.pop(node)

            if node == endWord:
                minlen = min(deapth[node], minlen)
                break

            for each in vertex:

                count = 0
                for i in range(size):
                    if each[i] != node[i]:
                        count += 1
                        if count > 1:
                            break
                if count == 1:
                    if not visisted[each]:
                        q.append(each)
                        visisted[each] = True
                    deapth[each] = min(deapth[node] + 1, deapth[each])


        if minlen == math.inf:
            return 0
        return minlen + 1

import collections

class optimal_Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        length = len(beginWord)
        dict = collections.defaultdict(list)
        for word in wordList:
            for i in range (length):
                new = word[:i] + '*' + word[i+1:]
                dict[new].append(word)
        visit = set()
        visit.add(beginWord)
        queue = collections.deque([(beginWord, 1)])
        while queue:
            cur, level = queue.popleft()
            for i in range (length):
                trans = cur[:i] + '*' + cur[i+1:]
                for word in dict[trans]:
                    if word == endWord:
                        return level + 1
                    if word not in visit:
                        queue.append((word, level+1))
                        visit.add(word)
        return 0