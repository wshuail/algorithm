#
# @lc app=leetcode.cn id=74 lang=python
#
# [74] 搜索二维矩阵
#
# https://leetcode-cn.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (45.02%)
# Total Accepted:    142.5K
# Total Submissions: 316.5K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 
# 
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -10^4 
# 
# 
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(matrix)-1
        index = 0
        while left <= right:
            mid = left + (right-left)//2
            # print (left, right, mid)
            if matrix[mid][-1] < target:
                left = mid+1
            elif matrix[mid][0] > target:
                right = mid-1
            else:
                index = mid
                break
        # print (index)

        left, right = 0, len(matrix[index])-1
        while left < right:
            mid = left + (right-left)//2
            if matrix[index][mid] < target:
                left = mid+1
            else:
                right = mid
        return matrix[index][left]==target







