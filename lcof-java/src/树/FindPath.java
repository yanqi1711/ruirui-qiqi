package 树;

import definition.TreeNode;

import java.util.ArrayList;

// 输入一颗二叉树的根节点root和一个整数expectNumber，找出二叉树中结点值的和为expectNumber的所有路径。
// 1.该题路径定义为从树的根结点开始往下一直到叶子结点所经过的结点
// 2.叶子节点是指没有子节点的节点
// 3.路径只能从父节点到子节点，不能从子节点到父节点
// 4.总节点数目为n
public class FindPath {
    private final ArrayList<ArrayList<Integer>> res = new ArrayList<>();
    /**
     * 二叉树中和为某一值的路径（二）
     */
    public ArrayList<ArrayList<Integer>> findPath(TreeNode root, int target) {
        if (root == null) {
            return new ArrayList<>();
        }
        ArrayList<Integer> path = new ArrayList<>();
        findAllPath(root, target, path);
        return res;
    }
    private void findAllPath(TreeNode root, int target, ArrayList<Integer> path) {
        if (root == null) {
            return;
        }
        // 遍历每一条路径，满足和为target加入list
        path.add(root.val);
        target -= root.val;
        if (target == 0 && root.left == null && root.right == null) {
            res.add(new ArrayList<>(path));
        }
        findAllPath(root.left, target, path);
        findAllPath(root.right, target, path);
        //  回溯
        path.remove(path.size() - 1);
    }
}
