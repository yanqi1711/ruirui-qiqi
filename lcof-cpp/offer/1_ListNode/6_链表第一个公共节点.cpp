/*
struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
            val(x), next(NULL) {
    }
};*/
class Solution
{
public:
    ListNode *FindFirstCommonNode(ListNode *pHead1, ListNode *pHead2)
    {
        if (!pHead1)
            return nullptr;
        if (!pHead2)
            return nullptr;
        ListNode *M = pHead1;
        ListNode *N = pHead2;
        while (M != N)
        {
            M = M ? M->next : pHead2; // 如果M为空才重置，否则正常移动
            N = N ? N->next : pHead1; // 如果N为空才重置，否则正常移动
        }
        return M;
    }
};
