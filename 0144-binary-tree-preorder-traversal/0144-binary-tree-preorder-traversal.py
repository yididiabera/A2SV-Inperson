# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        cur = root

        while cur or stack:
            if cur:
                stack.append(cur.right)
                result.append(cur.val)
                cur = cur.left
            else:
                cur = stack.pop()
        
        return result

        
        # answer = []
        # def helper(node):
        #     if node:
        #         answer.append(node.val)
        #         helper(node.left)
        #         helper(node.right)
        # helper(root)
        # return answer

        # answer = []
        # if root == None:
        #     return answer

        # answer.append(root.val) 
        # left_ans = self.preorderTraversal(root.left)
        # answer.extend(left_ans)
        # right_ans =self.preorderTraversal(root.right)
        # answer.extend(right_ans)
        # return answer