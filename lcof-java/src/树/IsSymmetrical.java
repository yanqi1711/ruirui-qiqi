package 树;

import definition.TreeNode;

// 给定一棵二叉树，判断其是否是自身的镜像（即：是否对称）
public class IsSymmetrical {
    /**
     * 对称的二叉树
     */
    public boolean isSymmetrical (TreeNode pRoot) {
        // write code here
        // 如果根结点为空，则返回true
        if (pRoot == null) return true;
        // 递归遍历判断是否左右孩子为镜像
        return recur(pRoot.left, pRoot.right);
    }
    // 判断两颗子树是否为镜像
    private boolean recur(TreeNode left, TreeNode right) {
        // 两结点都为空返回true
        if (left == null && right == null) return true;
        // 两结点有一个不为空或者值不相等返回false
        if (left == null || right == null || left.val != right.val) return false;
        // 递归遍历对称的结点
        return recur(left.left, right.right) && recur(left.right, right.left);
    }
}
