# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_same = True
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> None:
            nonlocal is_same
            if not p and not q:
                return None
            elif not p or not q:
                is_same = False
                return None
            if p.val != q.val:
                is_same = False

            dfs(p.left,q.left)
            dfs(p.right,q.right)
        dfs(p,q)
        return is_same
