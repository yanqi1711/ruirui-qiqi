package 链表;

import definition.ListNode;

// 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针
public class DeleteDuplication {
    /**
     * 删除链表中重复的结点
     */
    public ListNode deleteDuplication(ListNode pHead) {
        if (pHead == null) return null;
        // 创建一个头结点
        ListNode res = new ListNode(0);
        res.next = pHead;
        ListNode cur = res;
        // 使用当前指针的后两个结点进行遍历
        while (cur.next != null && cur.next.next != null) {
            // 遇到两个相邻结点值相同
            if (cur.next.val == cur.next.next.val) {
                int temp = cur.next.val;
                // 跳过所有相同的
                while (cur.next != null && cur.next.val == temp) {
                    cur.next = cur.next.next;
                }
            } else {
                cur = cur.next;
            }
        }
        // 返回时去掉头结点
        return res.next;
    }
}
