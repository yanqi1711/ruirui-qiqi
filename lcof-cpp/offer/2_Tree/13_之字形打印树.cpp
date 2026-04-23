/**
 * struct TreeNode {
 *  int val;
 *  struct TreeNode *left;
 *  struct TreeNode *right;
 *  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */
#include <deque>
#include <vector>
class Solution
{
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     *
     * @param pRoot TreeNode类
     * @return int整型vector<vector<>>
     */
    vector<vector<int>> Print(TreeNode *pRoot)
    {
        if (!pRoot)
            return {};
        bool flag = true;
        vector<vector<int>> res;
        deque<TreeNode *> dq;
        dq.emplace_back(pRoot);
        while (!dq.empty())
        {
            vector<int> ans;
            int lelvelSize = dq.size();
            for (int i = 0; i < lelvelSize; ++i)
            {
                if (flag)
                {
                    TreeNode *node = dq.front();
                    dq.pop_front();
                    ans.emplace_back(node->val);
                    if (node->left)
                        dq.emplace_back(node->left);
                    if (node->right)
                        dq.emplace_back(node->right);
                }
                else
                {
                    TreeNode *node = dq.back();
                    dq.pop_back();
                    ans.emplace_back(node->val);
                    // 因为下一次肯定是反过来的 所以插入顺序也要反过来
                    if (node->right)
                        dq.emplace_front(node->right);
                    if (node->left)
                        dq.emplace_front(node->left);
                }
            }
            flag = !flag; //! 逻辑反 ~按位反
            res.emplace_back(ans);
        }
        return res;
    }
};