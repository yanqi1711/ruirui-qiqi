package 树;

import definition.TreeNode;

// 输入两棵二叉树A，B，判断B是不是A的子结构。（我们约定空树不是任意一个树的子结构）
public class HasSubtree {
    /**
     * 树的子结构
     */
    public boolean hasSubtree(TreeNode root1, TreeNode root2) {
        if (root1 == null || root2 == null) {
            return false;
        }
        return recur(root1, root2) || hasSubtree(root1.left, root2) || hasSubtree(root1.right, root2);
    }

    private boolean recur (TreeNode A, TreeNode B) {
        // 如果B为空，说明当前遍历完毕，返回true
        if (B == null) return true;

        // 如果A为空或者A结点值与B结点值不同返回false
        if (A == null || A.val != B.val) return false;

        // 上面判断完毕说明当前两结点的值相等，递归判断A的子结构与B的子结构是否一样
        return recur(A.left, B.left) && recur(A.right, B.right);
    }
}
