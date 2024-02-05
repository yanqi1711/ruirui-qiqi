package 栈和队列;

import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;

// 给定一个长度为 n 的数组 num 和滑动窗口的大小 size ，找出所有滑动窗口里数值的最大值。
// 例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
// 窗口大于数组长度或窗口长度为0的时候，返回空。
public class MaxInWindows {
    /**
     * 滑动窗口的最大值
     */
    // region 暴力计算
    public ArrayList<Integer> maxInWindows (int[] num, int size) {
        ArrayList<Integer> res = new ArrayList<>();
        if (size > num.length || size == 0) return res;
        // 计算出一共有count个滑动窗口
        int count = num.length - size + 1;
        // 找出每个滑动窗口中的最大值
        for (int i = 0; i < count; i++) {
            int maxNumber = num[i];
            for (int j = 0; j < size; j++) {
                if (num[i + j] > maxNumber) {
                    maxNumber = num[i + j];
                }
            }
            res.add(maxNumber);
        }
        return res;
    }
    // endregion

    // region 双端队列
    public ArrayList<Integer> maxInWindowsOptimize (int[] num, int size){
        ArrayList<Integer> res = new ArrayList<>();
        if (size > num.length || size == 0) return res;

        Deque<Integer> deque = new LinkedList<>();
        // 初始化双端队列
        for (int i = 0; i < size; i++) {
            // 移除当前队列末尾开始存储的下标所指向数组中的元素值小于当前数的数据
            while (!deque.isEmpty() && num[i] > num[deque.peekLast()]) {
                deque.pollLast();
            }
            // 确认当前数是所记录的最小值后，将当前当前数据的下标插入队列末尾
            deque.offerLast(i);
        }
        // 处理滑动窗口
        for (int i = size; i < num.length; i++) {
            res.add(num[deque.peekFirst()]);
            while (!deque.isEmpty() && num[i] > num[deque.peekLast()]) {
                deque.pollLast();
            }
            // 移除已经脱离滑动窗口的下标
            if (!deque.isEmpty() && deque.peekFirst() <= i - size) {
                deque.pollFirst();
            }
            deque.offerLast(i);
        }
        res.add(num[deque.peekFirst()]);

        return res;
    }
    // endregion
}
