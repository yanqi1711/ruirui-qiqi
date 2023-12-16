package 树;

import definition.TreeLinkNode;
import java.util.ArrayList;

// 给定一个二叉树其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
// 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的next指针。
public class GetNext {
    /**
     * 二叉树的下一个结点
     */
    public TreeLinkNode getNext(TreeLinkNode pNode) {
        ArrayList<TreeLinkNode> list = new ArrayList<>();
        TreeLinkNode tmp = pNode;
        while (pNode.next != null) pNode = pNode.next;

        // 中序遍历获得排序好的列表
        inOrder(pNode, list);
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i) == tmp) {
                // 输入节点的下一个节点即为目标
                return list.get(i + 1);
            }
        }
        return null;
    }

    // 中序遍历，将节点存入列表
    private void inOrder(TreeLinkNode root, ArrayList<TreeLinkNode> list) {
        if (root == null) return;
        inOrder(root.left, list);
        list.add(root);
        inOrder(root.right, list);
    }
}
