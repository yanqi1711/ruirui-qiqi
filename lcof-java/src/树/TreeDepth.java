package 树;

import definition.TreeNode;

import java.util.LinkedList;
import java.util.Queue;

// 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径
// 最长路径的长度为树的深度，根节点的深度视为 1 。
public class TreeDepth {
    /**
     * 二叉树的深度
     */
    public int treeDepth(TreeNode root) {
        if (root == null) return 0;
        // 记录深度
        int count = 0;
        // 队列维护当前层的结点
        Queue<TreeNode> q = new LinkedList<>();
        // 根节点入队
        q.offer(root);
        // 层次遍历
        while (!q.isEmpty()) {
            // 记录当前层结点数
            int n = q.size();
            // 遍历当前层，再进入下一层
            for (int i = 0; i < n; i++) {
                TreeNode node = q.poll();
                if (node.left != null) {
                    q.offer(node.left);
                }
                if (node.right != null) {
                    q.offer(node.right);
                }
            }
            // 深度加1
            count++;
        }
        return count;
    }

    /**
     * 二叉树的深度
     * 解法二（推荐）
     */
    public int maxDepth (TreeNode root) {
        //空节点没有深度
        if(root == null)
            return 0;
        //返回子树深度+1
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    }
}
