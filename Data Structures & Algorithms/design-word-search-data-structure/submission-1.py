class PTNode:
    def __init__(self):
        self.tail = False
        self.next = {}



class WordDictionary:

    def __init__(self):
        self.head = PTNode()

    def addWord(self, word: str) -> None:
        th = self.head
        for ch in word:
            if not th.next.get(ch,None):
                th.next[ch] = PTNode()
            th = th.next[ch]
        th.tail = True
            
    def search(self, word: str) -> bool:
        th = self.head
        q = [th]
        l = len(word)
        for idx, ch in enumerate(word):
            temp = []
            if ch == '.':
                for node in q:
                    temp.extend(node.next.values())
            else:
                for node in q:
                    if node.next.get(ch,None):
                        temp.append(node.next[ch])
            q = temp
            if not q and idx == l - 1:
                return False
        return any([item.tail for item in q])
