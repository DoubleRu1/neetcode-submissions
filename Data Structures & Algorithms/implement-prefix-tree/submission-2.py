class TreeNode:
    def __init__(self,val:str = None):
        self.val = None
        self.children = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.Tree = TreeNode()

    def insert(self, word: str) -> None:
        head = self.Tree
        for ch in word:
            if ch not in head.children.keys():
                head.children[ch] = TreeNode(ch)
            head = head.children[ch]
        head.is_end = True


    def search(self, word: str) -> bool:
        head = self.Tree
        for idx,ch in enumerate(word):
            if ch not in head.children.keys():
                return False
            if idx == len(word)-1:
                return head.children[ch].is_end
            head = head.children[ch]
        return False

    def startsWith(self, prefix: str) -> bool:
        head = self.Tree
        for idx,ch in enumerate(prefix):
            if ch not in head.children.keys():
                return False
            # if idx == len(prefix)-1:
            #     return not head.children[ch].is_end
            head = head.children[ch]
        return True
        