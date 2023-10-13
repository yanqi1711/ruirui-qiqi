package 链表;

import definition.ListNode;

import java.util.LinkedList;

// 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
public class ReversePrint {
    /**
     * 从尾到头打印链表
     * @param head 链表头结点
     * @return 反转后放入数组
     */
    public int[] reversePrint(ListNode head) {
        if (head == null) return new int[0];
        LinkedList<Integer> integers = new LinkedList<>();
        int len = 0;
        while(head.next != null) {
            integers.add(head.val);
            head = head.next;
            len++;
        }
        integers.add(head.val);
        len++;
        int[] ans = new int[len];
        for (int i = 0; i < len; ++i) {
            ans[i] = integers.get(len - i - 1);
        }
        return ans;
    }
}