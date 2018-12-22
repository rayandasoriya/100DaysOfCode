# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return []
        
        queue = [root]
        res = []
        
        while queue:
            node = queue.pop(0)
            if val> node.val and node.right:
                queue.append(node.right)
            if val < node.val and node.left:
                queue.append(node.left)
        
            if val == node.val:
                res = node

            
    return res
