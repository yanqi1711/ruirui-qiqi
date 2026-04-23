/**
 * struct ListNode {
 *  int val;
 *  struct ListNode *next;
 *  ListNode(int x) : val(x), next(nullptr) {}
 * };
 */
#include <vector>
class Solution
{
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param lists ListNode类vector
     * @return ListNode类
     */

    ListNode *Merge2(ListNode *pHead1, ListNode *pHead2)
    {
        if (pHead1 == nullptr)
            return pHead2;
        if (pHead2 == nullptr)
            return pHead1;
        auto *head = new ListNode(-1);
        ListNode *cur = head;
        while (pHead1 && pHead2)
        {
            if (pHead1->val <= pHead2->val)
            {
                cur->next = pHead1;
                pHead1 = pHead1->next;
            }
            else
            {
                cur->next = pHead2;
                pHead2 = pHead2->next;
            }
            cur = cur->next;
        }
        if (pHead1)
            cur->next = pHead1;
        else
            cur->next = pHead2;
        return head->next;
    }

    ListNode *divideMerge(vector<ListNode *> &lists, int left, int right)
    {
        if (left > right)
            return nullptr;
        else if (left == right)
            return lists[left];
        int mid = (left + right) / 2;
        return Merge2(divideMerge(lists, left, mid), divideMerge(lists, mid + 1,
                                                                 right));
    }

    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        return divideMerge(lists, 0, lists.size() - 1);
    }
};