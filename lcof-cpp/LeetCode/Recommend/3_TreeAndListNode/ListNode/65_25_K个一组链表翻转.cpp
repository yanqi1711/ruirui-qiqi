//  Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    pair<ListNode *, ListNode *> myReverse(ListNode *head, ListNode *tail)
    {
        // 反转之后 头结点第一个就连上了尾巴
        ListNode *prev = tail->next;
        // 头要进行反转
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
        auto dummyHead = new ListNode(-1);
        dummyHead->next = head;
        ListNode *pre = dummyHead;
        while (head)
        {
            // 记录前一个结点 经过k个之后这个结点就是当前需要的翻转的结点
            ListNode *tail = pre;
            for (int i = 0; i < k; ++i)
            {
                tail = tail->next;
                if (!tail)
                {
                    return dummyHead->next;
                }
            }
            // myReverse后 tail变成了 头结点
            auto result = myReverse(head, tail);
            // 反转了 需要更新头
            head = result.first;
            tail = result.second;
            // 更新连接
            pre->next = head;
            pre = tail;
            head = tail->next;
        }
        return dummyHead->next;
    }
};