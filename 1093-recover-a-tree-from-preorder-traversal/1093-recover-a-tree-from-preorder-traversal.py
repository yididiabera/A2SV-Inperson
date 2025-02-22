# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        n = len(traversal)

        while i < n:
            depth = 0
            # Count dashes to determine depth
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Extract the number
            num = 0
            while i < n and traversal[i].isdigit():
                num = num * 10 + int(traversal[i])
                i += 1
            
            # Create new node
            node = TreeNode(num)
            
            # Maintain proper parent-child relationships
            while len(stack) > depth:
                stack.pop()
            
            if stack:
                parent = stack[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            
            # Push the node onto the stack
            stack.append(node)
        
        return stack[0]  # Root of the tree
