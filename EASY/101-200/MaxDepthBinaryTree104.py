# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def search(node, depth):
            if not node:
                return depth

            depth += 1

            left = search(node.left, depth)
            right = search(node.right, depth)

            return max(left, right)
        
        return search(root, 0)
