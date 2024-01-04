package 栈和队列;

import java.util.Stack;

// 例如，"coder. a am I"
// 正确的句子应该是"I am a coder."
public class ReverseSentence {
    /**
     * 翻转单词序列
     */
    // region 自己的思路
    public String reverseSentence(String str) {
        if (str == null) return null;
        Stack<Character> stack = new Stack<>();
        StringBuilder res = new StringBuilder();
        // coder. a am I -> .redoc a ma I
        // 将每个单词的顺序反转，则整个字符串目前都是反的
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) != ' ') {
                stack.push(str.charAt(i));
            } else {
                while (!stack.isEmpty()) {
                    res.append(stack.pop());
                }
                res.append(' ');
            }
        }
        while (!stack.isEmpty()) {
            res.append(stack.pop());
        }
        return res.reverse().toString();
    }
    // endregion

    // region 优化版
    public String reverseSentenceOptimize(String str) {
        Stack<String> stack = new Stack<>();
        String[] temp = str.split(" ");
        // 单词加入栈中
        for (String s : temp) {
            stack.push(s);
            stack.push(" ");
        }
        StringBuilder res = new StringBuilder();
        if (!stack.isEmpty()) {
            stack.pop();
        }
        // 根据栈的特性，弹出后单词的顺序后更正过来
        while (!stack.isEmpty()) {
            res.append(stack.pop());
        }
        return res.toString();
    }
    // endregion
}
