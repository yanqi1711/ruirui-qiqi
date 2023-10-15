package 链表;

import definition.ListNode;

// 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。返回删除后的链表的头节点。
public class DeleteNode {
    /**
     * 删除链表的节点
     * @param head ListNode类
     * @param val int整型
     * @return ListNode类
     */
    public ListNode deleteNode (ListNode head, int val) {
        // write code here
        if (head == null) return null;
        ListNode res = new ListNode(0);
        ListNode temp;
        res.next = head;
        temp = res;
        while (head.next != null) {
            // 如果出现与目标值一致的，直接跳过该结点
            if (head.val == val) {
                temp.next = head.next;
            } else {
                temp = temp.next;
            }
            head = head.next;
        }
        return res.next;
    }
}
