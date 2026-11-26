# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        num = []
        flag = True
        def inorder(root):
            nonlocal num
            nonlocal flag
            if not root:
                return None
            inorder(root.left)
            if num and num[-1] >= root.val:
                flag = False
            num.append(root.val)
            inorder(root.right)
        inorder(root)

        return flag
        