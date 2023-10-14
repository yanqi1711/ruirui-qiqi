package 链表;

import definition.RandomListNode;

import java.util.HashMap;
import java.util.Map;

// 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
// 另一个特殊指针random指向一个随机节点），请对此链表进行深拷贝，并返回拷贝后的头结点。
// （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）。
public class Clone {
    private Map<RandomListNode, RandomListNode> map = new HashMap<>();

    /**
     * 复杂链表的复制
     * @param pHead 目标链表
     * @return 复制的结果
     */
    public RandomListNode clone(RandomListNode pHead) {
        //终止条件next给过来的node为null
        if (pHead == null){
            return null;
        }

        //中间处理方法
        //1.递归创建节点到最后一个节点，并把所有创建的节点保存在map中
        RandomListNode copy = new RandomListNode(pHead.label);
        map.put(pHead, copy);
        copy.next = clone(pHead.next);
        //2.因为递归过程中会创建所有的节点，所以回溯过程中直接进行copy.random赋值
        copy.random = map.get(pHead.random);
        return copy;
    }
}
