package 树;

import definition.TreeNode;
import java.util.HashMap;

// 给定节点数为 n 的二叉树的前序遍历和中序遍历结果，请重建出该二叉树并返回它的头结点。
public class ReConstructBinaryTree {
    /**
     * 重建二叉树
     */
    public TreeNode reConstructBinaryTree(int[] preOrder, int[] vinOrder) {
        // 利用HashMap存储中序遍历数组的值与索引的对应关系，加速查找
        HashMap<Integer, Integer> indexMap = new HashMap<>();
        for (int i = 0; i < vinOrder.length; i++) {
            indexMap.put(vinOrder[i], i);
        }

        return buildTree(preOrder, 0, preOrder.length - 1, vinOrder, 0, vinOrder.length - 1, indexMap);
    }

    private TreeNode buildTree(int[] preOrder, int preStart, int preEnd, int[] vinOrder, int vinStart, int vinEnd, HashMap<Integer, Integer> indexMap) {
        if (preStart > preEnd || vinStart > vinEnd) {
            return null;
        }

        int rootValue = preOrder[preStart];
        TreeNode root = new TreeNode(rootValue);

        int rootIndexInVin = indexMap.get(rootValue);
        int leftTreeSize = rootIndexInVin - vinStart;

        root.left = buildTree(preOrder, preStart + 1, preStart + leftTreeSize, vinOrder, vinStart, rootIndexInVin - 1, indexMap);
        root.right = buildTree(preOrder, preStart + leftTreeSize + 1, preEnd, vinOrder, rootIndexInVin + 1, vinEnd, indexMap);

        return root;
    }
}
