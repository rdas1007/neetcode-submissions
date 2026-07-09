class Node():
    def __init__(self):
        self.children = {}
        self.eow = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = Node()
            curr = curr.children[w]
        curr.eow = True

    def search(self, word: str) -> bool:
        def dfs(w, curr):
            if w == len(word):
                print(w, curr.children, curr.eow)
                return curr.eow
            # print(w, curr.children)
            if word[w] == '.':
                for c in curr.children:
                    if dfs(w+1, curr.children[c]):
                        return True
                return False
            else:
                if word[w] in curr.children:
                    return dfs(w+1, curr.children[word[w]])
                else:
                    return False
        return dfs(0, self.root)
