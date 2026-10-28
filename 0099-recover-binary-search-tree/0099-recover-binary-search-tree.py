# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None 
        second = None
        prev = None
        def inorder(root):
            nonlocal first,second,prev
            if root is None:
                return 
            inorder(root.left)
            if prev and prev.val>root.val:
                if first is None:
                    first = prev
                second = root
            prev = root
            inorder(root.right)
        inorder(root)
        first.val,second.val = second.val,first.val


        