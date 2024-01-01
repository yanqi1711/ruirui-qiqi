package 栈和队列;

import java.util.Stack;

// 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的 min 函数
// 输入操作时保证 pop、top 和 min 函数操作时，栈中一定有元素
public class MinStack {
    /**
     * 包含min函数的栈
     */
    Stack<Integer> stack = new Stack<>();
    public void push(int node) {
        stack.push(node);
    }

    public void pop() {
        stack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int min() {
        return stack.stream().min(Integer::compareTo).orElse(Integer.MAX_VALUE);
    }
}
