# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     QuickSelect
   Description :
   Author :       zdf
   date：          2018/9/26
-------------------------------------------------
   Change Activity:
                   2018/9/26:13:11
-------------------------------------------------
"""


def partition(test, left, right, mid):
    tmp = test[mid]
    while left < right:
        while test[right] > tmp and left < right:
            right -= 1
        while test[left] < tmp and left < right:
            left += 1
        if left < right:
            test[left], test[right] = test[right], test[left]
            right -= 1
            left += 1
    return mid


def quickselect(test, left, right, k):
    if left == right:
        return test[left]
    mid = (left + right) // 2
    mid = partition(test, left, right, mid)
    if k == mid:
        return test[k]
    if k < mid:
        return quickselect(test, left, mid - 1, k)
    if k > mid:
        return quickselect(test, mid + 1, right, k)


if __name__ == "__main__":
    test = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    print("Sorted list:", sorted(test))
    for k in range(1,12):
        print("The", k, "th smallest number is", quickselect(test, 0, len(test) - 1, k))
