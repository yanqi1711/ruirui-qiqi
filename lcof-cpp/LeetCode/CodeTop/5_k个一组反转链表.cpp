/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    pair<ListNode *, ListNode *> myReverse(ListNode *head, ListNode *tail)
    {
        ListNode *prev = tail->next; // 反转链表I 这里是nullptr 因为nullptr就是反转链表I的尾巴结点 这个其实才是任意2个结点间反转
        // 头部要反转
        ListNode *p = head;
        while (prev != tail)
        {
            ListNode *nex = p->next;
            p->next = prev;
            prev = p;
            p = nex;
        }
        return {tail, head};
    }
    ListNode *reverseKGroup(ListNode *head, int k)
    {
        ListNode *dummyHead = new ListNode(-1);
        dummyHead->next = head;
        ListNode *pre = dummyHead; // 因为头结点开始就要反转
        while (head)
        {
            ListNode *tail = pre; // 要反转结点前的头结点
            for (int i = 0; i < k; ++i)
            {
                tail = tail->next;
                if (!tail)
                    return dummyHead->next; // 没有k个结点了 结束
            }
            auto result = myReverse(head, tail);
            // 实际链表头已经反转了 但是还是更新 符合循环
            head = result.first;
            tail = result.second;
            // 更新
            pre->next = head;
            pre = tail;
            head = tail->next;
        }
        return dummyHead->next;
    }
};