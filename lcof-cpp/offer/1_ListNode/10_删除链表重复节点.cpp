
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
    ListNode *deleteDuplication(ListNode *pHead)
    {
        if (pHead == nullptr)
            return nullptr;
        auto *res = new ListNode(0);
        // 在链表前加一个表头
        res->next = pHead;
        ListNode *cur = res;
        while (cur->next != nullptr && cur->next->next != nullptr)
        {
            if (cur->next->val == cur->next->next->val)
            {
                int temp = cur->next->val;
                // 将所有相同的都跳过
                while (cur->next && cur->next->val == temp)
                {
                    // next相等了， 直接跳过这个
                    cur->next = cur->next->next;
                }
            }
            else
            {
                // 不相等 直接更新
                cur = cur->next;
            }
        }
        return res->next;
    }
};