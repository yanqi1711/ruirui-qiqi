package 树;

import definition.TreeNode;

import java.util.LinkedList;
import java.util.Queue;

// 请实现两个函数，分别用来序列化和反序列化二叉树
// 不对序列化之后的字符串进行约束，但要求能够根据序列化之后的字符串重新构造出一棵与原二叉树相同的树
public class Codec {
    /**
     * 序列化二叉树
     */
    public String serialize(TreeNode root) {
        if (root == null) return "[]";
        StringBuilder res = new StringBuilder("[");
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        // 层序遍历，如果当前结点为空则记录为#,如果不为空则记录下当前值并让左右孩子入队
        while (!queue.isEmpty()){
            TreeNode node = queue.poll();
            if (node != null) {
                res.append(node.val).append(",");
                queue.offer(node.left);
                queue.offer(node.right);
            } else {
                res.append("#,");
            }
        }
        res.deleteCharAt(res.length() - 1);
        res.append("]");
        return res.toString();
    }

    /**
     * 二叉树的反序列化
     */
    public TreeNode deserialize(String str) {
        if (str.equals("[]")) return null;
        String[] vals = str.substring(1, str.length() - 1).split(",");
        TreeNode root = new TreeNode(Integer.parseInt(vals[0]));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int i = 1;
        // 层序遍历，找到不为空的结点添加给当前出队的结点的左右孩子，并入队
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (!vals[i].equals("#")) {
                node.left = new TreeNode(Integer.parseInt(vals[i]));
                queue.offer(node.left);
            }
            i++;
            if (!vals[i].equals("#")) {
                node.right = new TreeNode(Integer.parseInt(vals[i]));
                queue.offer(node.right);
            }
            i++;
        }
        return root;
    }
}
