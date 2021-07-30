# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/612/week-5-july-29th-july-31st/3832/
# https://leetcode.com/problems/map-sum-pairs/

class MapSum:

    def __init__(self):
        from collections import defaultdict
        self.data = [{}]
        self.node = 0
        self.value = defaultdict(int)

    def insert(self, key, val):
        curr_node = 0
        for i in key:
            if i not in self.data[curr_node]:
                self.node += 1
                self.data[curr_node][i] = self.node
                self.data.append({})
            curr_node = self.data[curr_node][i]
        self.value[curr_node] = val

    def sum(self, prefix):
        curr_node = 0
        val = 0
        for i in prefix:
            if i in self.data[curr_node]:
                curr_node = self.data[curr_node][i]
            else:
                return val

        def dfs(currnode):
            nonlocal val

            if currnode in self.value:
                val += self.value[currnode]

            if not len(self.data[currnode]):
                return

            for each in self.data[currnode]:
                dfs(self.data[currnode][each])

        dfs(curr_node)

        return val