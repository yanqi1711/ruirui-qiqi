package 链表;

import definition.ListNode;

import java.util.HashSet;

// 给一个长度为n链表，若其中包含环，请找出该链表的环的入口结点，否则，返回null。
public class EntryNodeOfLoop {
    /**
     * 链表中环的入口结点
     * @param pHead 目标链表
     * @return 入口结点
     */
    public ListNode entryNodeOfLoop(ListNode pHead) {
        HashSet<ListNode> hashSet = new HashSet<>();
        while (pHead != null) {
            if (hashSet.contains(pHead)) {
                return pHead;
            }
            hashSet.add(pHead);
            pHead = pHead.next;
        }
        return null;
    }
}
