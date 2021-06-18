"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        queue = [(root, 1)]
        max_depth = 1
        
        while queue:
            node,depth = queue.pop()
            max_depth = max(depth, max_depth)
            for child in node.children:
                queue.append((child, depth+1))
        return max_depth