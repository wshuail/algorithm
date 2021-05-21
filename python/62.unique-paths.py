#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# https://leetcode-cn.com/problems/unique-paths/description/
#
# algorithms
# Medium (64.85%)
# Total Accepted:    251.8K
# Total Submissions: 386.8K
# Testcase Example:  '3\n7'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
# 
# 问总共有多少条不同的路径？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：m = 3, n = 7
# 输出：28
# 
# 示例 2：
# 
# 
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
# 
# 
# 示例 3：
# 
# 
# 输入：m = 7, n = 3
# 输出：28
# 
# 
# 示例 4：
# 
# 
# 输入：m = 3, n = 3
# 输出：6
# 
# 
# 
# 提示：
# 
# 
# 1 
# 题目数据保证答案小于等于 2 * 10^9
# 
# 
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.d = {}
        return self.dfs(m=m, n=n, h=1, w=1)

    def dfs(self,m, n, h, w):
        if (h, w) in self.d:
            return self.d[(h, w)]
        if h==m or w==n:
            return 1
        self.d[(h, w)] = self.dfs(m, n, h+1, w) + self.dfs(m, n, h, w+1)
        return self.d[(h, w)]

"""
m, n = 23, 12
sol = Solution()
print (sol.uniquePaths(m, n))
"""





