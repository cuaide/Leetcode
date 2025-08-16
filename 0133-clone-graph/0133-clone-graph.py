"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visit = set()
        visit.add(node)
        queue = deque()
        queue.add(node)

        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur = target:
                    return 
            for neighbor in node[node]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)

        return visit