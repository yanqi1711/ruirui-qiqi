#include <unordered_map>
using namespace std;
struct myListNode
{
    int key;
    int val;
    myListNode *prev;
    myListNode *next;
    myListNode(int key, int val)
        : key(key), val(val), prev(nullptr), next(nullptr) {}
};
class LRUCache
{

public:
    unordered_map<int, myListNode *> mp;
    myListNode *head = nullptr;
    myListNode *tail = nullptr;
    int capacity;
    int size;
    LRUCache(int capacity)
    {
        this->capacity = capacity;
        this->size = 0;
        head = new myListNode(-1, -1); // 头结点
        tail = new myListNode(-1, -1); // 尾结点
        head->next = tail;
        tail->prev = head;
    }
    ~LRUCache()
    {
        myListNode *current = head;
        while (current != nullptr)
        {
            myListNode *temp = current;
            current = current->next;
            delete temp;
        }
    }
    int get(int key)
    {
        if (mp.find(key) != mp.end())
        {
            moveToFront(mp[key]);
            return mp[key]->val;
        }
        return -1;
    }

    void put(int key, int value)
    {
        // 检查键是否已存在
        if (mp.find(key) != mp.end())
        {
            // 存在：更新值并将节点移动到链表头
            mp[key]->val = value;
            moveToFront(mp[key]);
            return;
        }
        // 不存在 就插入
        myListNode *node = new myListNode(key, value);
        if (size >= capacity)
        {
            // 满了 删除尾巴
            myListNode *toRemove = tail->prev;
            mp.erase(toRemove->key);  // 移出map
            deleteListNode(toRemove); // 断开连接
            // 此时tail->prev变了
            delete toRemove; // 实际删除内存都在put里面
            --size;
        }
        insertListNode(node);
        mp[key] = node;
        ++size;
        return;
    }

    void insertListNode(myListNode *node)
    {
        // 插入一定是在头结点插入
        if (!node)
            return;
        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
        return;
    }
    void deleteListNode(myListNode *node)
    {
        node->prev->next = node->next;
        node->next->prev = node->prev;
        // 注意：在这里不要 delete node，因为在 put 函数中，node 可能还会被使用
        // 例如，在 moveToFront 中，我们先删除节点，然后再插入
        // 所以在 deleteListNode 中不 delete node，而在 put 函数中删除
        return;
    }
    void moveToFront(myListNode *node)
    {
        if (!node)
            return;
        // 先从当前位置删除
        deleteListNode(node);
        // 再插入到头部
        insertListNode(node);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */