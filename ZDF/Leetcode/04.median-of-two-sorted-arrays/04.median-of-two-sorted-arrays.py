# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     04.median-of-two-sorted-arrays
   Description :
   Author :       zdf's desktop
   date：          2018/10/29
-------------------------------------------------
   Change Activity:
                   2018/10/29:18:52
-------------------------------------------------
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        # return nums
        # return length

        if length % 2 == 1:
            return nums[length // 2] / 1.0
        else:
            return (nums[length // 2] + nums[length // 2 - 1]) / 2.0