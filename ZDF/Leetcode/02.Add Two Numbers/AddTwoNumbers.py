# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     AddTwoNumbers
   Description :
   Author :       zdf's desktop
   date：          2018/10/29
-------------------------------------------------
   Change Activity:
                   2018/10/29:18:46
-------------------------------------------------
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        up = 0
        ans = p = ListNode(0)
        while l1 or l2 or up:
            v1 = v2= 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            up, val = divmod(v1 + v2 + up, 10)
            p.next = ListNode(val)
            p = p.next
        return ans.next