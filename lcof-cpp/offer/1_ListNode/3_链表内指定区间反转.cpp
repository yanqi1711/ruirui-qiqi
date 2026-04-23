/**
 * struct ListNode {
 *	int val;
 *	struct ListNode *next;
 *	ListNode(int x) : val(x), next(nullptr) {}
 * };
 */
#include <memory>
class Solution
{
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param head ListNode类
     * @param m int整型
     * @param n int整型
     * @return ListNode类
     */
    ListNode *reverseBetween(ListNode *head, int m, int n)
    {
        if (!head)
            return nullptr;
        auto dummyHead = new ListNode(-1);
        dummyHead->next = head;
        auto pre = dummyHead; // 记录要更改区间的前一个节点
        for (int i = 0; i < m - 1; ++i)
            pre = pre->next;
        // 类似插入排序 将第一个一次一次 反转到最后， 但是要把最后的向前反转 所以每一次反转都要把cur_next节点向最开始的位置反转
        auto cur = pre->next; // 要反转到最后的节点
        ListNode *cur_next = nullptr;
        for (int i = 0; i < n - m; ++i)
        {
            // 更新cur_next结点
            cur_next = cur->next;
            cur->next = cur_next->next; // 将cur->next连接指向下一个节点
            cur_next->next = pre->next; // 反转到第一个结点 类似LRUcache的moveToFront
            pre->next = cur_next;
        }
        return dummyHead->next;
    }
};