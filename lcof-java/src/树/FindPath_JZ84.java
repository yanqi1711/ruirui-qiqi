package 树;

import definition.TreeNode;

// 给定一个二叉树root和一个整数值 sum ，求该树有多少路径的的节点值之和等于sum
// 1.该题路径定义不需要从根节点开始，也不需要在叶子节点结束，但是一定是从父亲节点往下到孩子节点
// 2.总节点数目为n
// 3.保证最后返回的路径个数在整形范围内(即路径个数小于231-1)
public class FindPath_JZ84 {
    /**
     * 二叉树中和为某一值的路径（三）
     */
    int res = 0;
    void dfs(TreeNode root, int sum) {
        if (root == null) return;
        if (sum == root.val) res++;
        dfs(root.left, sum - root.val);
        dfs(root.right, sum - root.val);
    }
    public int findPath (TreeNode root, int sum) {
        if (root == null) {
            return res;
        }
        dfs(root, sum);
        findPath(root.left, sum);
        findPath(root.right, sum);
        return res;
    }
}
