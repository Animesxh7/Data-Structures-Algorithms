# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
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
        mini = float('inf')
        for i in range(len(a)-1):
            mini = min(mini,a[i+1]-a[i])
        return mini
