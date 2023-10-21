package 树;

import definition.TreeNode;
import java.util.ArrayList;
import java.util.Collections;

// 给定一棵结点数为n 二叉搜索树，请找出其中的第 k 小的TreeNode结点值。
// 1.返回第k小的节点值即可
// 2.不能查找的情况，如二叉树为空，则返回-1，或者k大于n等等，也返回-1
// 3.保证n个节点的值不一样
public class KthNode {
    ArrayList<Integer> list = new ArrayList<>();
    /**
     * 二叉搜索树的第k个节点
     */
    public int kthNode (TreeNode proot, int k) {
        // write code here
        preOrder(proot);
        int len = list.size();
        if (len < k || k < 0 || proot == null) {
            return  -1;
        }
        Collections.sort(list);
        return list.get(k - 1);
    }

    // 前序遍历
    private void preOrder(TreeNode root) {
        if (root == null) {
            return;
        }
        list.add(root.val);
        preOrder(root.left);
        preOrder(root.right);
    }
}
