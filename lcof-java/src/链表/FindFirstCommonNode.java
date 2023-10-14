package 链表;

import definition.ListNode;

// 输入两个无环的单向链表，找出它们的第一个公共结点，如果没有公共节点则返回空。
public class FindFirstCommonNode {
    /**
     * 两个链表的第一个公共结点
     * @param pHead1 链表1
     * @param pHead2 链表2
     * @return 第一个公共结点
     */
    public ListNode findFirstCommonNode(ListNode pHead1, ListNode pHead2) {
        if (pHead1 == null || pHead2 == null) return null;
        ListNode node1 = pHead1;
        ListNode node2 = pHead2;
        // 判断两结点是否相等
        while (node1 != node2) {
            // 如果遍历完链表1，则继续遍历链表2
            node1 = (node1 == null) ? pHead2 : node1.next;
            // 如果遍历完链表2，则继续遍历链表1
            node2 = (node2 == null) ? pHead1 : node2.next;
        }
        return node1;
    }
}
