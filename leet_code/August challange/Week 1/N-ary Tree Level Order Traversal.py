# https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3871/

<<<<<<< HEAD
=======

>>>>>>> deab56880a408cf319ce8826c1989e75b6a9293a
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

<<<<<<< HEAD
=======

>>>>>>> deab56880a408cf319ce8826c1989e75b6a9293a
class Solution:
    def levelOrder(self, root):
        from collections import defaultdict, deque
        if not root:
            return []
        level = defaultdict(lambda: 0)
        result = defaultdict(list)
        q = deque()
        q.append(root)
        level[root] = 0
        visited = set()
        visited.add(root)
        while q:
            node = q.popleft()
            result[level[node]].append(node.val)

            for each in node.children:
                level[each] = level[node] + 1
                if each not in visited:
                    q.append(each)
                    visited.add(each)

        print(list(result.values()))
        return list(result.values())
