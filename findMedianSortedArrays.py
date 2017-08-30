# -*- coding:utf-8 -*-
'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

'''
    难度:中
    
    1.先去科普了下中位数,就是求一个有序序列的中间一位数(序列个数为奇数)的值或中间两个数(序列个数为偶数)的和除2
    2.先合并两个序列,然后排序
    3.判度序列元素个数是否为偶数,是的话就取元素个数除2的值为序列下标加上除2-1的下标所对应的值再除2得到中位数
    4.元素个数为奇数的话,获取个数除2下标对应值就OK
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            return (nums1[int((len(nums1) / 2.0))] + nums1[int((len(nums1) / 2) - 1)]) / 2.0
        else:
            return nums1[(len(nums1) / 2)]


b = Solution()
print b.findMedianSortedArrays([1,2], [3,4])
