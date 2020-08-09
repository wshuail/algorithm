#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Given an array of integers, every element appears twice except for one. Find that single one.


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]
        return ans


