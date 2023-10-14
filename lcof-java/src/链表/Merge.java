package 链表;

import definition.ListNode;

//输入两个递增的链表，单个链表的长度为n，合并这两个链表并使新链表中的节点仍然是递增排序的。
public class Merge {
    /**
     * 合并两个排序的链表
     * @param pHead1 链表1
     * @param pHead2 链表2
     * @return 合并后的链表
     */
    public ListNode merge (ListNode pHead1, ListNode pHead2) {
        // write code here
        // 定义一个头节点dum，节点cur指向dum
        ListNode dum = new ListNode(0);
        ListNode cur = dum;
        // 循环合并
        while (pHead1 != null && pHead2 != null) {
            if (pHead1.val < pHead2.val) {
                cur.next = pHead1;
                pHead1 = pHead1.next;
            }
            else {
                cur.next = pHead2;
                pHead2 = pHead2.next;
            }
            cur = cur.next;
        }
        // 三元判断合并其余节点
        cur.next = pHead1 != null ? pHead1 : pHead2;
        return dum.next;
    }
}
