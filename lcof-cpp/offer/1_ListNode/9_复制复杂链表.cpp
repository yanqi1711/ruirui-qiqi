/*
struct RandomListNode {
    int label;
    struct RandomListNode *next, *random;
    RandomListNode(int x) :
            label(x), next(NULL), random(NULL) {
    }
};
*/
#include <unordered_map>
class Solution
{
public:
    RandomListNode *Clone(RandomListNode *pHead)
    {
        if (!pHead)
            return pHead;
        // 把原来的记住 直接new一个新的就行了
        unordered_map<RandomListNode *, RandomListNode *> mp;
        auto dummy = new RandomListNode(0); // 哨兵节点

        RandomListNode *pre = dummy,
                       *cur = pHead; // 指向哨兵和链表头的指针
        while (cur)
        {
            auto *clone = new RandomListNode(cur->label); // 拷贝节点
            pre->next = clone;                            // 与上个结点连接
            mp[cur] = clone;                              // 记录映射关系
            pre = pre->next;                              // 指针移动
            cur = cur->next;
        }
        for (auto &[key, value] : mp)
        { // 遍历哈希表
            value->random = key->random == nullptr ? nullptr : mp[key->random];
        }

        delete dummy; // 释放哨兵节点空间
        return mp[pHead];
    }
};