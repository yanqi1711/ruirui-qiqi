/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};*/
class Solution
{
public:
    bool isSame(TreeNode *root, TreeNode *node)
    {
        // 节点没了肯定是true
        if (!node)
            return true;
        // 前面已经判定node存在 root没了 返回false
        if (!root)
            return false;
        if (root->val != node->val)
            return false;

        return isSame(root->left, node->left) && isSame(root->right, node->right);
    }
    bool HasSubtree(TreeNode *pRoot1, TreeNode *pRoot2)
    {
        if (!pRoot1)
            return false;
        // pRoot2是没有的 但是上一个if 得到的pRoot1是存在的
        if (!pRoot2)
            return false;
        return isSame(pRoot1, pRoot2) || HasSubtree(pRoot1->left, pRoot2) || HasSubtree(pRoot1->right, pRoot2);
    }
};
