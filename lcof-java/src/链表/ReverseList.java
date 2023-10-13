package 链表;

import definition.ListNode;

// 反转链表
public class ReverseList {
    /**
     * 反转链表
     * @param head 链表头结点
     * @return 反转后的链表头结点
     */
    public static ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode tmp = curr;
            curr = curr.next;
            tmp.next = prev;
            prev = tmp;
        }
        return prev;
    }
}
