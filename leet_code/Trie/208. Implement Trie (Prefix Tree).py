# https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie:

    def __init__(self):
        self.is_word = {0: False}
        self.prefixadjlist = [{}]
        self.vertex = 0

    def insert(self, word: str) -> None:

        node = 0
        for i in range(len(word)):
            if word[i] not in self.prefixadjlist[node]:
                self.vertex += 1
                self.prefixadjlist[node][word[i]] = self.vertex
                self.prefixadjlist.append({})
            node = self.prefixadjlist[node][word[i]]
        self.is_word[node] = True

    def search(self, word: str) -> bool:
        node = 0
        i = 0
        l = len(word)
        found = False

        def dfs(node, i):
            nonlocal word, found
            if i == l:
                if node in self.is_word:
                    found = True
                    return
                else:
                    return False

            if word[i] == '.':
                for each in self.prefixadjlist[node].values():
                    if not found:
                        dfs(each, i + 1)

            else:
                if word[i] in self.prefixadjlist[node] and not found:
                    dfs(self.prefixadjlist[node][word[i]], i + 1)

        dfs(0, 0)
        return found

    def startsWith(self, prefix: str) -> bool:
        node = 0
        i = 0
        l = len(prefix)
        found = False

        def dfs(node, i):
            nonlocal prefix, found
            if i == l:
                found = True
                return

            if prefix[i] in self.prefixadjlist[node] and not found:
                dfs(self.prefixadjlist[node][prefix[i]], i + 1)

        dfs(0, 0)
        return found


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("jyoti")
print(obj.search("jyoti"))
print(obj.startsWith("jy"))