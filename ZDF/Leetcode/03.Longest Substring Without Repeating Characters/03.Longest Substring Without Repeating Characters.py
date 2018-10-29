# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     03.Longest Substring Without Repeating Characters
   Description :
   Author :       zdf's desktop
   date：          2018/10/29
-------------------------------------------------
   Change Activity:
                   2018/10/29:18:52
-------------------------------------------------
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxL = 0
        used = {}
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                maxL = max(maxL, i - start + 1)
            used[s[i]] = i
            # print "maxL=" + str(maxL) + " start=" + str(start)
        # print used
        return maxL