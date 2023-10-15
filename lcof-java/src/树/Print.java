package 树;

import definition.TreeNode;

import java.util.*;

// 给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）
public class Print {
    /**
     * 按之字形顺序打印二叉树
     * @param pRoot TreeNode类
     * @return int整型ArrayList<ArrayList<>>
     */
    public ArrayList<ArrayList<Integer>> print (TreeNode pRoot) {
        // write code here
        TreeNode head = pRoot;
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        if (head == null) return res;
        // 使用队列做层序遍历
        Queue<TreeNode> temp = new LinkedList<>();
        temp.offer(head);
        TreeNode p;
        boolean flag = true;
        while (!temp.isEmpty()) {
            // 记录二叉树的某一行
            ArrayList<Integer> row = new ArrayList<>();
            int n = temp.size();
            // 第一行不反转
            flag = !flag;
            for (int i = 0; i < n; i++) {
                p = temp.poll();
                row.add(p.val);
                if (p.left != null) {
                    temp.offer(p.left);
                }
                if (p.right != null) {
                    temp.offer(p.right);
                }
            }
            if (flag) {
                Collections.reverse(row);
            }
            res.add(row);
        }
        return res;
    }
}
