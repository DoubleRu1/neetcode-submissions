# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # iterate the first tree, find the second tree root
        pro_roots = []
        def find_root(root: Optional[TreeNode], target: Optional[TreeNode]) -> None:
            nonlocal pro_roots
            if not root or not target:
                return None
            if root.val == target.val:
                pro_roots.append(root)
            left = find_root(root.left,target)
            right = find_root(root.right,target)
        find_root(root,subRoot)
        # print(pro_roots)        
        # if match
        def match(source: Optional[TreeNode], target: Optional[TreeNode]) -> bool:
            if not source and not target:
                return True
            elif not source or not target:
                return False
            elif source.val != target.val:
                return False
            
            left = match(source.left,target.left)
            right = match(source.right,target.right)

            if left and right:
                return True
            else:
                return False

        
        return any([match(pro_root,subRoot) for pro_root in pro_roots])
            
