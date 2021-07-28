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
    def ladderLength(self, beginWord, endWord, wordList):
        from collections import defaultdict, deque
        l = len(endWord)
        if endWord not in wordList:
            return []
        intermediate_words = defaultdict(list)
        for each in wordList:
            for i in range(l):
                word = each[:i] + "*" + each[i + 1:]
                intermediate_words[word].append(each)

        q = deque()
        q.append(beginWord)
        level = defaultdict(int)
        visited = {beginWord: True}
        while len(q):
            node = q.popleft()
            if node == endWord:
                return level[node] + 1

            for i in range(l):
                word = node[:i] + "*" + node[i + 1:]

                for each in intermediate_words[word]:
                    if each not in visited:
                        visited[each] = True
                        q.append(each)
                        level[each] = level[node] + 1

        return 0