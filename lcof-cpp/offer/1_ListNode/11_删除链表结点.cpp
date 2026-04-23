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
     * @param head ListNode类
     * @param val int整型
     * @return ListNode类
     */
    ListNode *deleteNode(ListNode *head, int val)
    {
        if (head == nullptr)
            return nullptr;
        auto dummyHead = new ListNode(-1);
        dummyHead->next = head;
        ListNode *pre = dummyHead;
        ListNode *cur = head;
        while (cur)
        {
            if (cur->val == val)
            {
                pre->next = cur->next;
                cur = cur->next;
                break;
            }
            else
            {
                cur = cur->next;
                pre = pre->next;
            }
        }
        return dummyHead->next;
    }
};