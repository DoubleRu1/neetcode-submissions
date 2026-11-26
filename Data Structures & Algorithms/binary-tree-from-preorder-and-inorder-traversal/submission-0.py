# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        tree = TreeNode(preorder[0])
        idx = 0
        while idx < len(inorder) and inorder[idx] != preorder[0]:
            idx += 1

        tree.left = self.buildTree(preorder[1:idx+1],inorder[0:idx])
        tree.right = self.buildTree(preorder[idx+1:],inorder[idx+1:])

        return tree

