# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None
        total = 0
        def inorder(root):
            nonlocal total
            if root is None:
                return 
            inorder(root.right)
            total += root.val
            root.val = total
            inorder(root.left)
        inorder(root)
        return root