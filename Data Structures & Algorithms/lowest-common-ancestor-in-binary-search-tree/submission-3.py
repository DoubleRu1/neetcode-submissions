# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> tuple(bool,bool):
        ans = []
        def post_order(root: TreeNode,p: TreeNode,q: TreeNode) -> None:
            nonlocal ans
            if not root:
                return False, False
            left_visited_p, left_visited_q = post_order(root.left,p,q,)
            right_visited_p, right_visited_q = post_order(root.right,p,q,)
            visited_p = left_visited_p or right_visited_p or root.val == p.val
            visited_q = left_visited_q or right_visited_q or root.val == q.val
            if visited_p and visited_q:
                ans.append(root)
            return  visited_p, visited_q
        post_order(root,p,q)
        return ans[0]



