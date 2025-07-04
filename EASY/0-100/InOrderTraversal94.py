# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        lit = []
            
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            lit.append(node.val)
            dfs(node.right)
        dfs(root)
        return lit

# [1,2,3,4,5,null,8,null,null,6,7,9]

# root = 1

# stack: 1
# 1.left = 2
# 2.left = 4
# 4.left = none
# 4.append
# 4.right = none
# 2.append
# 2.right = 5
# 5.left = 6
# 6.left = none
# 6.append
# 6.right = none
# 5.append
# 5.right = 7
# 7.left = none
# 7.append
# 7.right = none
# 1.append
# 1.right = 3
# 3.left = none
# 3.append
# 3.right = 8
# 8.left = 9
# 9.left = none
# 9.append
# 9.right = none
# 8.append
# 8.right = none
# complete



# return = 4,2,6,5,7,1,3,9,8