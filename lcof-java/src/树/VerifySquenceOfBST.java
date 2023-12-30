package 树;

// 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
// 如果是则返回 true ,否则返回 false 。假设输入的数组的任意两个数字都互不相同。
public class VerifySquenceOfBST {
    /**
     * 二叉搜索树的后序遍历序列
     */
    public boolean verifySequenceOfBST(int[] sequence) {
        int n = sequence.length;
        // 空树不是二叉搜索树，返回false
        if (n == 0) return false;
        return check(sequence, 0, n-1);
    }

    // 检查数组是否是二叉搜索树的后序遍历序列
    private boolean check(int[] sequence, int left, int right) {
        // 若当前子树只有一个节点
        if (left >= right) return true;

        // 当前子树的根结点
        int root = sequence[right];
        // 比根节点大的结点可划分为二叉搜索树的右子树
        int j = right - 1;
        while (j >=0 && sequence[j] > root) j--;

        // 检查左子树是否存在比根节点大的数
        for (int i = left; i <= j; i++) {
            if (sequence[i] > root) return false;
        }

        // 分治法检查左子树和右子树
        return
            check(sequence, left, j) &&
            check(sequence, j+1, right-1);
    }
}
