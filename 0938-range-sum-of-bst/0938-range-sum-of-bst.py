# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        if root is None:
            return 0
        a = []
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            a.append(root.val)
            inorder(root.right)
        inorder(root)
        sumi = 0
        for i in a:
            if low<=i<=high:
                sumi += i
        return sumi
            
            
        
