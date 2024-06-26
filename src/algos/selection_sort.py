from src.algos.util.helper import swap
from typing import List


def selection_sort(arr: List[int], direction='ASC', generate = False):
  """O(n^2)"""
  n = len(arr)
  for i in range(n):
    min_index = i
    min_value = arr[min_index]
    for j in range(i+1, n):
      if direction == 'ASC':
        if arr[j] < min_value:
          min_index = j
          min_value = arr[min_index]
      elif direction == 'DESC':
        if arr[j] > min_value:
          min_index = j
          min_value = arr[min_index]
    swap(arr, i, min_index)
    if generate:
      yield i, min_index