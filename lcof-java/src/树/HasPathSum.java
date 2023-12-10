package 树;

import definition.TreeNode;

// 给定一个二叉树root和一个值 sum ，判断是否有从根节点到叶子节点的节点值之和等于 sum 的路径。
// 1.该题路径定义为从树的根结点开始往下一直到叶子结点所经过的结点
// 2.叶子节点是指没有子节点的节点
// 3.路径只能从父节点到子节点，不能从子节点到父节点
// 4.总节点数目为n
public class HasPathSum {
    /**
     * 二叉树中和为某一值的路径（一）
     */
    public boolean hasPathSum (TreeNode root, int sum) {
        // 如果root为空，则返回false
        if (root == null) {
            return false;
        }
        // 如果root的左子树和右子树都为空，且root的值等于sum，则返回true
        if (root.left == null && root.right == null && root.val == sum) {
            return true;
        }
        // 递归遍历左右子树，如果有一条可以满足总值为sum，就返回true
        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
    }
}
