package 树;

import definition.TreeNode;

// 操作给定的二叉树，将其变换为源二叉树的镜像。
public class Mirror {
    /**
     * 二叉树的镜像
     */
    public TreeNode mirror (TreeNode pRoot) {
        // write code here
        // 当该结点为空时终止本次遍历
        if (pRoot == null) {
            return null;
        }
        // 递归遍历整个二叉树
        mirror(pRoot.left);
        mirror(pRoot.right);

        // 交换该结点的左右子树
        TreeNode temp = pRoot.left;
        pRoot.left = pRoot.right;
        pRoot.right = temp;
        // 返回该结点
        return pRoot;
    }
}
