# -*- coding:utf-8 -*-
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

'''
    难度:简单
    
    1.采用冒泡算法,依次对比就能很容易做出来了!
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in xrange(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]