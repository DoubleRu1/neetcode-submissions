# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False
        def preorder(root):
            nonlocal ans
            if not root or ans:
                return
            # print(root.val, subRoot.val)
            if root.val == subRoot.val:
                ans = isSame(root,subRoot)
            preorder(root.left)
            preorder(root.right)
        def isSame(root, subRoot):
            if root == None and subRoot == None:
                return True
            if root == None or subRoot == None:
                return False
            left = isSame(root.left, subRoot.left)
            right = isSame(root.right, subRoot.right)
            return left and right and root.val == subRoot.val
        preorder(root)
        return ans
        

        
        