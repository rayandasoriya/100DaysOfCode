class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        TreeNode left = root.left;
        TreeNode right = root.right;
        int acc = 2;
        while (left != null && right != null) {
            left = left.left;
            right = right.right;
            acc *= 2;
        }
        if (left == right) {
            // in fact it's left = right = null
            return acc - 1;
        } else {
            return 1 + countNodes(root.left) + countNodes(root.right);
    }
}
}
