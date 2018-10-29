# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MinPrefixSubarray
   Description :
   Author :       zdf's desktop
   date：          2018/10/9
-------------------------------------------------
   Change Activity:
                   2018/10/9:16:57
-------------------------------------------------
"""


def mps(a, left, right):
    if left == right:
        return a[left]
    else:
        mid = (right + left) // 2
        return min(mps(a, left, mid), mps(a, mid + 1, right) + sum(a[left:(mid + 1)]))


if __name__ == "__main__":
    nums = [4, 2, 6, -3, -5, -7, -8, -3, 4, 6, -10, -1]
    print(mps(nums, 0, 11))
