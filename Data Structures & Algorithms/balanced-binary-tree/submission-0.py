# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True
        def height(root: Optional[TreeNode]) -> int:
            nonlocal balance
            if not root: return 0
            left = height(root.left) + 1
            right = height(root.right) + 1
            if abs(left-right) > 1:
                balance = False
            return max(left,right)
        height(root)
        return balance

