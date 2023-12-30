package 树;

import definition.TreeNode;

import java.util.ArrayList;

// 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
// 1.对于该题的最近的公共祖先定义:对于有根树T的两个节点p、q，最近公共祖先LCA(T,p,q)表示一个节点x，
// 满足x是p和q的祖先且x的深度尽可能大。在这里，一个节点也可以是它自己的祖先.
// 2.二叉搜索树是若它的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
// 若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值
// 3.所有节点的值都是唯一的。
// 4.p、q 为不同节点且均存在于给定的二叉搜索树中。
public class LowestCommonAncestor_JZ68 {
    /**
     * 二叉搜索树的最近公共祖先
     */
    public ArrayList<Integer> getPath(TreeNode root, int target) {
        ArrayList<Integer> path = new ArrayList<>();
        TreeNode node = root;
        //节点值都不同，可以直接用值比较
        while(node.val != target){
            path.add(node.val);
            //小的在左子树
            if(target < node.val)
                node = node.left;
                //大的在右子树
            else
                node = node.right;
        }
        path.add(node.val);
        return path;
    }
    public int lowestCommonAncestor(TreeNode root, int p, int q) {
        //求根节点到两个节点的路径
        ArrayList<Integer> path_p = getPath(root, p);
        ArrayList<Integer> path_q = getPath(root, q);
        int res = 0;
        //比较两个路径，最后一个相同的节点
        for(int i = 0; i < path_p.size() && i < path_q.size(); i++){
            int x = path_p.get(i);
            int y = path_q.get(i);
            //最后一个相同的节点就是最近公共祖先
            if(x == y)
                res = path_p.get(i);
            else
                break;
        }
        return res;
    }
}
