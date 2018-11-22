class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def trav(root):
            if not root.left and not root.right:
                return
            if not root.next:
                root.left.next = root.right
                root.right.next = None
            else:
                root.left.next = root.right
                root.right.next = root.next.left
            trav(root.left)
            trav(root.right)
        if not root:
            return
        root.next = None
        trav(root)
