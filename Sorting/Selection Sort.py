# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:40:49 2022

@author: Avinash Kumar
"""

def selectionSort(array):
    cIdx = 0
    while cIdx < len(array) - 1:
        sIdx = cIdx
        for i in range(cIdx + 1, len(array)):
            if array[sIdx] > array[i]:
                sIdx = i
        swap(cIdx, sIdx, array)
        cIdx += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [8, 5, 2, 9, 5, 6, 3]
res = selectionSort(array)
print(res)