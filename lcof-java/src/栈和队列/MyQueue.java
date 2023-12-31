package 栈和队列;

import java.util.Stack;

// 用两个栈来实现一个队列，使用n个元素来完成 n 次在队列尾部插入整数(push)和n次在队列头部删除整数(pop)的功能
// 队列中的元素为int类型。保证操作合法，即保证pop操作时队列内已有元素
public class MyQueue {
    // 用两个栈实现队列
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();

    public void push(int node) {
        stack1.push(node);
    }

    public int pop() {
        // 如果当前stack2中没有节点了代表此时的节点都在stack1中，需要压栈到stack2中
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
        return stack2.pop();
    }
}
