/**
 * struct TreeNode {
 *  int val;
 *  struct TreeNode *left;
 *  struct TreeNode *right;
 *  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */
#include <limits>
#include <type_traits>
#include <vector>
class Solution
{
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param root TreeNode类
     * @param p int整型
     * @param q int整型
     * @return int整型
     */
    void get_path(TreeNode *root, int p, vector<int> &v)
    {
        if (!root)
            return;
        while (root && root->val != p)
        {
            v.emplace_back(root->val);
            if (root->val < p)
                root = root->right;
            else
                root = root->left;
        }
        if (root)
            v.emplace_back(root->val);
    }
    int lowestCommonAncestor(TreeNode *root, int p, int q)
    {
        vector<int> vp;
        vector<int> vq;
        get_path(root, p, vp);
        get_path(root, q, vq);
        // 因为有公共祖先 那么前面的一定相等
        int i = 0, res = -1;
        while (i < vp.size() && i < vq.size())
        {
            if (vp[i] == vq[i])
            {
                res = vp[i];
                ++i;
            }
            else
            {
                break;
            }
        }
        return res;
    }
};