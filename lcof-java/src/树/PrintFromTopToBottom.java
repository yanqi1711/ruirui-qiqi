package 树;

import definition.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

// 不分行从上往下打印出二叉树的每个节点，同层节点从左至右打印。
// 例如输入{8,6,10,#,#,2,1}，
// 则依次打印8,6,10,2,1(空节点不打印，跳过)，请你将打印的结果存放到一个数组里面，返回。
public class PrintFromTopToBottom {
    /**
     * 从上往下打印二叉树
     */
    public ArrayList<Integer> printFromTopToBottom(TreeNode root) {
        if (root == null)
            return new ArrayList<>();
        ArrayList<Integer> res = new ArrayList<>();
        // 使用队列做层序遍历
        Queue<TreeNode> list = new LinkedList<>();
        list.offer(root);
        while (!list.isEmpty()) {
            int temp = list.size();
            for (int i = 0; i < temp; i++) {
                TreeNode node = list.poll();
                res.add(node.val);
                if (node.left != null) {
                    list.offer(node.left);
                }
                if (node.right != null) {
                    list.offer(node.right);
                }
            }
        }
        return res;
    }
}
