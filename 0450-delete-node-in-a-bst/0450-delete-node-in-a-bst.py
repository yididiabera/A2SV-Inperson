# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        def findNode(node):
            while node.next:
                node = node.next
            return node
        
        def delete(root, key):
            if not root:
                return root
            
            if key < root.val:
                root.left = delete(root.left, key)
            elif key > root.val:
                root.right = delete(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right: 
                    return root.left
                else:
                    node = findNode(root.right)
                    root.val = node.val
                    root.right = delete(root.right, node.val)

            return root

        def findNode(node):
            while node.left:
                node = node.left
            return node

        return delete(root, key)
