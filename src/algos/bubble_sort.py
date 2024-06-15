from src.algos.util.helper import swap
from typing import List


def swap(arr: List[int], index_0: int, index_1: int):
  """Swap two array indices values, list is passed by reference"""
  arr[index_0], arr[index_1] = arr[index_1], arr[index_0]

def bubble_sort(arr: List[int]):
  """O(n^2)"""
  for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
      if arr[j] > arr[j+1]:
        swap(arr, j, j+1)
  return arr

if __name__ == "__main__":
  pass
  # print(UNSORTED)
  # bubble_sort(UNSORTED)
  # print(UNSORTED)
  # arr = [1, 2]
  # swap(arr, 0, 1)
  # print(arr)