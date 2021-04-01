#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# https://leetcode-cn.com/problems/min-stack/description/
#
# algorithms
# Easy (56.03%)
# Total Accepted:    219.9K
# Total Submissions: 389.3K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
#  '[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 
# 
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。
# 
# 
# 
# 
# 示例:
# 
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
# 
# 
# 
# 
# 提示：
# 
# 
# pop、top 和 getMin 操作总是在 非空栈 上调用。
# 
# 
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def push(self, val: int) -> None:
        self.l.append(val)

    def pop(self) -> None:
        if not self.l:
            return 'error'
        return self.l.pop(-1)

    def top(self) -> int:
        if not self.l:
            return 'error'
        return self.l[-1]


    def getMin(self) -> int:
        if not self.l:
            return 'error'
        return min(self.l)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
