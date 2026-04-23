
/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};
*/
class Solution
{
public:
    ListNode *EntryNodeOfLoop(ListNode *pHead)
    {
        if (!pHead || !pHead->next || !pHead->next->next)
            return nullptr;
        ListNode *slow = pHead;
        ListNode *fast = pHead;
        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast)
            {
                fast = pHead;
                break;
            }
        }
        if (fast != pHead)
            return nullptr;
        while (slow != fast)
        {
            slow = slow->next;
            fast = fast->next;
        }
        return slow;
    }
};