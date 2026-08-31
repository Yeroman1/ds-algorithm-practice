# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):

        stack = []
        result = []

        if root is None:
            return result

        stack.append(root)

        while stack:

            temp = stack.pop()

            if temp.right:
                stack.append(temp.right)

            if temp.left:
                stack.append(temp.left)

            result.append(temp.val)

        return result    