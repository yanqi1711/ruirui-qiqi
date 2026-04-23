/**
 * struct ListNode {
 *	int val;
 *	struct ListNode *next;
 *	ListNode(int x) : val(x), next(nullptr) {}
 * };
 */
class Solution
{
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param pHead ListNode类
     * @param k int整型
     * @return ListNode类
     */
    ListNode *FindKthToTail(ListNode *pHead, int k)
    {
        if (!pHead)
            return nullptr;
        ListNode *pre = pHead, *after = pHead;
        int x = 0;
        while (x < k)
        {
            if (after == nullptr)
                return nullptr;
            after = after->next;
            ++x;
        }
        while (after)
        {
            pre = pre->next;
            after = after->next;
        }
        return pre;
    }
};