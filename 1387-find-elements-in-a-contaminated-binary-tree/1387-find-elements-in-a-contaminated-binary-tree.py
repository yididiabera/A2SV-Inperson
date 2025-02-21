# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.recovered_values = set()
        self.recover_tree(root, 0)  # Start recovery from root with value 0

    def recover_tree(self, node: Optional[TreeNode], value: int):
        if not node:
            return
        node.val = value
        self.recovered_values.add(value)
        self.recover_tree(node.left, 2 * value + 1)
        self.recover_tree(node.right, 2 * value + 2)

    def find(self, target: int) -> bool:
        return target in self.recovered_values
