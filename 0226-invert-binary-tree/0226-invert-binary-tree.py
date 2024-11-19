# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        if not root:
            return

        temp = root.left
        root.left = root. right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# A single recursive call can only process one node or subtree at a time.
# You must process both the left and right subtrees independently to fully invert the tree.
# because the parameter (root) handles one node at a time, you need two recursive calls: