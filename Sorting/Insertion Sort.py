# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:30:31 2022

@author: Avinash Kumar
"""

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j-=1
    return array
            
            
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

array = [8, 5, 2, 9, 5, 6, 3]
res = insertionSort(array)
print(res)
