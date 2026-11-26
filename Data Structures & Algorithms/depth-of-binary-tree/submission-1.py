# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def postorder(root):
            if not root:
                return 0
            left, right = 0, 0
            if root.left:
                left = postorder(root.left) + 1
            if root.right:
                right = postorder(root.right) + 1
            return max(left, right, 0)
        return postorder(root) + 1

