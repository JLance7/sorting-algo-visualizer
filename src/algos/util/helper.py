from typing import List


def swap(arr: List[int], index_0: int, index_1: int):
  """Swap two array indices values, list is passed by reference"""
  arr[index_0], arr[index_1] = arr[index_1], arr[index_0]