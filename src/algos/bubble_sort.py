from src.algos.util.helper import swap
from typing import List

def bubble_sort(arr: List[int]):
  """O(n^2)"""
  for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
      if arr[j] > arr[j+1]:
        swap(arr, j, j+1)
  return arr

# if __name__ == "__main__":
#   # bubble_sort()
#   arr = [1, 2]
#   swap(arr, 0, 1)
#   print(arr)