from typing import List
from src.algos.util.helper import swap


def insertion_sort(arr: List[int]):
  """O(n^2)"""
  n = len(arr)
  if n == 1:
    return arr
  for i in range(1, n):
    current = arr[i]
    j = i - 1
    prev = arr[j]

    while j >= 0 and current < prev:
      swap(arr, i, j)
      j -= 1
      prev = arr[j]
      i -= 1
      current = arr[i]

