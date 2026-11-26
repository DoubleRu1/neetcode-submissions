# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def preorder(root,pm):
            nonlocal ans
            if not root:
                return 
            if root.val >= pm:
                ans += 1
            preorder(root.left,max(root.val,pm))
            preorder(root.right,max(root.val,pm))
        
        preorder(root,float('-inf'))
        return ans