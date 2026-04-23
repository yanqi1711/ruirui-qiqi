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
    ListNode *partation(vector<ListNode *> &v, int left, int right)
    {
        if (right == left)
            return v[left];
        if (left < right)
        {
            int mid = left + (right - left) / 2;
            ListNode *leftList = partation(v, left, mid);
            ListNode *rightList = partation(v, mid + 1, right);
            return mergeList(leftList, rightList);
        }
        return nullptr;
    }
    ListNode *mergeList(ListNode *left, ListNode *right)
    {
        if (!left)
            return right;
        if (!right)
            return left;
        auto dummyHead = new ListNode(-1);
        ListNode *cur = dummyHead;
        while (left && right)
        {
            if (left->val <= right->val)
            {
                cur->next = left;
                left = left->next;
            }
            else
            {
                cur->next = right;
                right = right->next;
            }
            cur = cur->next;
        }
        cur->next = (left ? left : right);
        ListNode *temp = dummyHead->next;
        delete (dummyHead);
        return temp;
    }

    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        if (lists.empty())
            return nullptr;
        // 左闭右闭
        ListNode *head = partation(lists, 0, lists.size() - 1);
        return head;
    }
};