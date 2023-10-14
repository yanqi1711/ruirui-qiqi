package 链表;

import definition.ListNode;

import java.util.LinkedList;

// 输入一个长度为 n 的链表，设链表中的元素的值为 ai ，返回该链表中倒数第k个节点。
// 如果该链表长度小于k，请返回一个长度为 0 的链表。
public class FindKthToTail {
    /**
     * 链表中倒数最后k个结点
     * @param pHead 目标链表
     * @param k int类型参数
     * @return 目标结点
     */
    public ListNode findKthToTail (ListNode pHead, int k) {
        // write code here
        if (pHead == null || k == 0) return null;
        // 使用栈来进行反方向遍历的操作
        LinkedList<ListNode> stack = new LinkedList<>();
        while (pHead != null) {
            stack.push(pHead);
            pHead = pHead.next;
        }
        if (stack.size() < k) {
            return null;
        }
        while (--k != 0) {
            stack.pop();
        }
        return stack.pop();
    }
}
