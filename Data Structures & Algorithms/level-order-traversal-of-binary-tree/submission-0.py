# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        queue = [root]
        while queue:
            next_level = []
            cur_level = []
            for cur in queue:
                cur_level.append(cur.val)
                if cur.left:
                    next_level.append(cur.left)
                if cur.right:
                    next_level.append(cur.right)
            ans.append(cur_level)
            queue = next_level
        return ans