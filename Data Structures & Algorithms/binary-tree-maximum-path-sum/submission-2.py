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
            cur = root.val
            cur += max(left,right,0)
            ans = max(left+right+root.val,left+root.val,right+root.val,root.val,ans)
            return cur

        postorder(root)
        return ans
