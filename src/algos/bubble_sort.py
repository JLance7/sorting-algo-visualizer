from src.algos.util.helper import swap
from typing import List, Callable


def bubble_sort(arr: List[int], direction='ASC', generate = False):
  """O(n^2)"""
  for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
      if direction == 'ASC':
        if arr[j] > arr[j+1]:
          swap(arr, j, j+1)
          if generate:
            yield (j, j+1)
      elif direction == 'DESC':
        if arr[j] < arr[j+1]:
          swap(arr, j, j+1)
          if generate:
            yield (j, j+1)
  return arr


if __name__ == "__main__":
  pass
  # arr = [1, 2]
  # swap(arr, 0, 1)
  # print(arr)