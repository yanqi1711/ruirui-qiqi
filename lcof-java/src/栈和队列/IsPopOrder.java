package 栈和队列;

import java.util.Stack;

// 输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
// 假设压入栈的所有数字均不相等。
// 例如序列1,2,3,4,5是某栈的压入顺序，
// 序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
// 但4,3,5,1,2就不可能是该压栈序列的弹出序列。
public class IsPopOrder {
    /**
     * 栈的压入、弹出序列
     */
    public boolean isPopOrder (int[] pushV, int[] popV) {
        int n = pushV.length;
        // 辅助栈
        Stack<Integer> stack = new Stack<>();
        // 定义入栈下标
        int j = 0;
        // 遍历出栈数组
        for (int i = 0; i < n; i++) {
            // 辅助栈为空或者栈顶不等于出栈数组的时候入栈
            while ((j < n) && (stack.isEmpty() || stack.peek() != popV[i])) {
                stack.push(pushV[j]);
                j++;
            }
            // 栈顶等于出栈数组当前下标值则出栈，否则该出栈序列是错误的
            if (stack.peek() == popV[i]) {
                stack.pop();
            } else {
                return false;
            }
        }
        return true;
    }
}
