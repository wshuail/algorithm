#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (46.25%)
# Total Accepted:    173.5K
# Total Submissions: 375K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明：叶子节点是指没有子节点的节点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数的范围在 [0, 10^5] 内
# -1000 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        min_depth = 1
        nodes = [root]

        while len(nodes) > 0:
            level_nodes = []
            for node in nodes:
                if node.left is None and node.right is None:
                    return min_depth
                if node.left:
                    level_nodes.append(node.left)
                if node.right:
                    level_nodes.append(node.right)
            nodes = level_nodes
            if len(nodes) > 0:
                min_depth += 1


