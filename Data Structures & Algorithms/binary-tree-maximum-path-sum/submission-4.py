# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def postorder(root):
            nonlocal ans
            if not root:
                return 0
            left = postorder(root.left)
            right = postorder(root.right)
            ans = max(ans,max(left,left+right,right,0)+root.val)
            return max(left,right,0) + root.val

        postorder(root)
        return ans
