package 树;

import definition.TreeNode;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

// 给定一个节点数为 n 二叉树，要求从上到下按层打印二叉树的 val 值，
// 同一层结点从左至右输出，每一层输出一行，将输出的结果存放到一个二维数组中返回。
public class LevelPrint {
    /**
     * 把二叉树打印成多行
     */
    public ArrayList<ArrayList<Integer>> levelPrint (TreeNode pRoot) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        if (pRoot == null) return res;
        // 使用队列做层序遍历
        Queue<TreeNode> list = new LinkedList<>();
        list.offer(pRoot);
        TreeNode p;
        while (!list.isEmpty()) {
            // 使用队列做层序遍历
            ArrayList<Integer> row = new ArrayList<>();
            // 记录该行节点的数目
            int n = list.size();
            for (int i = 0; i < n; i++) {
                p = list.poll();
                row.add(p.val);
                if (p.left != null) {
                    list.offer(p.left);
                }
                if (p.right != null) {
                    list.offer(p.right);
                }
            }
            res.add(row);

        }
        return res;
    }
}
