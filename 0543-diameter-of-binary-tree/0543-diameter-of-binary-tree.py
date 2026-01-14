# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            lh, ld = dfs(node.left)
            rh, rd = dfs(node.right)
            
            h = 1 + max(lh, rh)
            dia = max(ld, rd, lh + rh)
            return h, dia
        return dfs(root)[1]
        