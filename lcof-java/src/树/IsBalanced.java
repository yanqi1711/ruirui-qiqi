package 树;

import definition.TreeNode;

// 输入一棵节点数为 n 二叉树，判断该二叉树是否是平衡二叉树。
// 在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
// 平衡二叉树（Balanced Binary Tree），具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，
// 并且左右两个子树都是一棵平衡二叉树。
public class IsBalanced {
    /**
     * 判断是不是平衡二叉树
     */
    public boolean isBalanced_Solution (TreeNode pRoot) {
        return recur(pRoot) != -1;
    }

    /**
     * 如果该树不是平衡二叉树，返回-1，是平衡二叉树，返回该树的高度
     */
    private int recur(TreeNode root) {
        // 节点为空，则返回0
        if (root == null) return 0;
        int left =  recur(root.left);
        if (left == -1) return -1;
        int right = recur(root.right);
        if (right == -1) return -1;
        // 该结点的左右子树的高度差的绝对值大于1，则返回-1，否则返回当前子树中的最大高度+1
        return Math.abs(left - right) > 1 ? -1 : Math.max(left, right) + 1;
    }
}