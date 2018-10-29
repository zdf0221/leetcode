# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     QuickSort
   Description :
   Author :       zdf's desktop
   date：          2018/9/19
-------------------------------------------------
   Change Activity:
                   2018/9/19:19:41
-------------------------------------------------
"""


def partition(a, left, right):
    mid = (left + right) // 2  # select the mid number as a pivot
    tmp = a[mid]
    while left < right:
        while a[right] > tmp and left < right:
            right -= 1
        while a[left] < tmp and left < right:
            left += 1
        if left < right:
            a[right], a[left] = a[left], a[right]  # swap the pair of unordered number
            right -= 1
            left += 1
    return mid


def quick_sort(a, left, right):
    if left >= right:
        return
    pivot = partition(a, left, right)
    quick_sort(a, left, pivot)
    quick_sort(a, pivot + 1, right)


if __name__ == "__main__":
    # test = [4, 3, 2, 1]
    test = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
    print("original:", test)
    quick_sort(test, 0, len(test) - 1)
    print("Sorted:", test)



