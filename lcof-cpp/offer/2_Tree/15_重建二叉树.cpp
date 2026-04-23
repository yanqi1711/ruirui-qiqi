/**
 * struct TreeNode {
 *  int val;
 *  struct TreeNode *left;
 *  struct TreeNode *right;
 *  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
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
     * @param preOrder int整型vector
     * @param vinOrder int整型vector
     * @return TreeNode类
     */
    TreeNode *reConstructBinaryTree(vector<int> &preOrder, vector<int> &vinOrder)
    {
        if (preOrder.empty())
            return nullptr;
        int n = preOrder.size();
        int m = vinOrder.size();
        auto root = new TreeNode(preOrder[0]);
        // 找中序遍历中间的根节点
        for (int i = 0; i < vinOrder.size(); ++i)
        {
            // 找到中序遍历的中点才能构建左右子树
            if (preOrder[0] == vinOrder[i])
            {
                // 构建左子树 前序遍历
                vector<int> leftpre(preOrder.begin() + 1, preOrder.begin() + i + 1);
                // 构建左子树 中序遍历
                vector<int> leftvin(vinOrder.begin(), vinOrder.begin() + i);
                root->left = reConstructBinaryTree(leftpre, leftvin);
                // 构建右子树 前序遍历
                vector<int> rightpre(preOrder.begin() + i + 1, preOrder.end());
                // 构建右子树 中序遍历 中间的已经构建节点了 所以+1
                vector<int> rightvin(vinOrder.begin() + i + 1, vinOrder.end());
                root->right = reConstructBinaryTree(rightpre, rightvin);
                break;
            }
        }
        return root;
    }
};