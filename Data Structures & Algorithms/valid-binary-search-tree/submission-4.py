# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True
        prevalue = -float('inf')
        def inorder(root):
            nonlocal ans,prevalue
            if not root:
                return
            left = inorder(root.left)
            if root.val <= prevalue:
                ans = False
            prevalue = root.val
            right = inorder(root.right)
        inorder(root)
        return ans
        
            
                