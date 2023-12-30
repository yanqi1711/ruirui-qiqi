package 树;

import definition.TreeNode;

import java.util.*;

// 给定一棵二叉树(保证非空)以及这棵树上的两个节点对应的val值 o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点
public class LowestCommonAncestor {
    /**
     * 在二叉树中找到两个节点的最近公共祖先
     */
    public int lowestCommonAncestor(TreeNode root, int o1, int o2) {
        // 记录遍历到的每个节点的父节点
        Map<Integer, Integer> parent = new HashMap<>();
        Queue<TreeNode> queue = new LinkedList<>();
        // 根结点没有父节点，给一个默认值
        parent.put(root.val, Integer.MIN_VALUE);
        queue.add(root);
        // BFS，直到两个节点都找到为止
        while (!parent.containsKey(o1) || !parent.containsKey(o2)) {
            TreeNode node = queue.poll();
            if (node.left != null) {
                parent.put(node.left.val, node.val);
                queue.add(node.left);
            }
            if (node.right != null) {
                parent.put(node.right.val, node.val);
                queue.add(node.right);
            }
        }
        Set<Integer> ancestors = new HashSet<>();
        // 记录下o1和他的祖先节点
        while (parent.containsKey(o1)) {
            ancestors.add(o1);
            o1 = parent.get(o1);
        }
        // 遍历o2和他的祖先节点，查看是否在o1到根节点的路径中，找出最近公共祖先
        while (!ancestors.contains(o2)) {
            o2 = parent.get(o2);
        }
        return o2;
    }
}
