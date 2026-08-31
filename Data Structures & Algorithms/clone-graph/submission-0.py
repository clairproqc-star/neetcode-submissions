"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldNewMap={}
        def dfs(node):
            if not node:
                return None
            if node in oldNewMap:
                return oldNewMap[node]
            else:
                copy=Node(node.val)
                oldNewMap[node]=copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)   