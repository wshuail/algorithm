#
# @lc app=leetcode.cn id=93 lang=python
#
# [93] 复原 IP 地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (53.04%)
# Total Accepted:    125.4K
# Total Submissions: 236.4K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
# 
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
# 
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
# 和 "192.168@1.1" 是 无效 IP 地址。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 
# 
# 示例 2：
# 
# 
# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 
# 
# 示例 3：
# 
# 
# 输入：s = "1111"
# 输出：["1.1.1.1"]
# 
# 
# 示例 4：
# 
# 
# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
# 
# 
# 示例 5：
# 
# 
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# s 仅由数字组成
# 
# 
#
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<4 or len(s)>12:
            return []

        path, res = [], []
        self.dfs(path, s, res)
        return res

    def is_valid(self, s):
        if not s:
            return False
        elif len(s) == 1:
            return True
        elif s[0] == '0':
            return False
        else:
            return 0<int(s)<=255

    def dfs(self, path, s, res):
        if len(path) > 4:
            return
        
        if not s and len(path)==4:
            res.append('.'.join(path))
            return

        tmp = ''
        for i in range(len(s)):
            tmp += s[i]
            if not self.is_valid(tmp):
                break
            path.append(tmp)
            self.dfs(path, s[i+1: ], res)
            path.pop()


"""
sol = Solution()
s = "25525511135"
# s = '00010'
res = sol.restoreIpAddresses(s)
print (res)
"""

