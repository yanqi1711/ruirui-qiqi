#include <bits/stdc++.h>
#include <algorithm>
#include <cstddef>
#include <vector>
struct ListNode
{
    int val;
    struct ListNode *next;
    ListNode(int x) : val(x), next(NULL)
    {
    }
};
class Solution
{
public:
    vector<int> printListFromTailToHead(ListNode *head)
    {
        // 如果头节点为空，直接返回空向量
        if (!head)
            return {};

        // 使用栈来存储节点值
        stack<int> s;
        ListNode *cur = head;

        // 遍历链表并将值压入栈中
        while (cur != nullptr)
        {
            s.push(cur->val);
            cur = cur->next;
        }
        // 创建结果向量，并从栈中弹出元素
        vector<int> v;
        while (!s.empty())
        {
            v.push_back(s.top());
            s.pop();
        }

        return v;
    }
};