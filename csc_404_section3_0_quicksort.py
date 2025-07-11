# -*- coding: utf-8 -*-
"""CSC_404_Section3_0_QuickSort.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T_wiC-gG8ZkKfZVfT3gMq1rw4cdkQcaF
"""

#import random

def quick_sort(L):
  n = len(L)
  if n <= 1:
    return L

  p = L.pop((n-1)//2)
  #p = L.pop(0) #first entry
  #p = L.pop() #last entry
  #p = L.pop(random.randint(0,n-1)) #random entry. Note - need to import random

  left = []
  right = []
  for x in L:
    if x < p:
      left.append(x)
    else:
      right.append(x)
  return quick_sort(left)+[p]+quick_sort(right)

print('Jenny\'s List!')
L = [4,8,6,7,5,3,0,9]
print('Unsorted List:\t',L)
print('Sorted List:\t',quick_sort(L))

import random

print('\nRandom List!')
L = [random.randint(0,100) for _ in range(100)]
print('Unsorted List:\t', L)
print('Sorted List:\t', quick_sort(L))

