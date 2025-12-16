# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia=0
        def height_bt(root):
            if root is None:
                return 0
            left_ht=height_bt(root.left)
            right_ht=height_bt(root.right)

            self.dia=max(self.dia,left_ht+right_ht)
            return 1+max(left_ht, right_ht)
        
        height_bt(root)
        return self.dia
        