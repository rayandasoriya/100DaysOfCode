def dfs_RLF(p,lst):
    if(p==None):
        lst.append(None)
        return None
    elif(p.left==None and p.right==None): # leaf node in the Base Case
        lst.append(p.val)
        return p.val
    else:
        lst.append(p.val)
        dfs_RLF(p.left,lst)
        dfs_RLF(p.right,lst)

class Solution(object):
    def isSameTree(self, p, q):
        """
            :type p: TreeNode
            :type q: TreeNode
            :rtype: bool
            """
        l1,l2 = [],[]
        dfs_RLF(p,l1)
        dfs_RLF(q,l2)
        
        print(l1)
        print(l2)
        
        return(l1==l2)
