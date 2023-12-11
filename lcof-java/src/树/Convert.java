package 树;

import definition.TreeNode;

import java.util.ArrayList;

// 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
public class Convert {
    ArrayList<TreeNode> list = new ArrayList<>();

    // 中序遍历，将二叉树的结点按顺序放入列表
    private void inOrder(TreeNode root) {
        if (root == null) return;

        inOrder(root.left);
        list.add(root);
        inOrder(root.right);
    }
    /**
     * 二叉搜索树与双向链表
     */
    public TreeNode convert(TreeNode pRootOfTree) {
        if (pRootOfTree == null) return null;
        // 中序遍历，排序
        inOrder(pRootOfTree);
        // 按顺序连接
        for (int i = 0; i < list.size() - 1; i++) {
            list.get(i).right = list.get(i+1);
            list.get(i+1).left = list.get(i);
        }
        return list.get(0);
    }
}
