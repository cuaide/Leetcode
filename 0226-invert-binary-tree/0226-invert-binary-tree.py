# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None 
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left # swap children.
            #after swapping, then append the children.
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
         