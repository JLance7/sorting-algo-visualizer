from src.algos.util.helper import swap
from src.algos import *

UNSORTED = [8, 2, 5, 9, 1, 4, 3, 5, 2]
SORTED =   [1, 2, 2, 3, 4, 5, 5, 8, 9]

def test_swap():
  arr = [1, 2]
  swap(arr, 0, 1)
  assert arr == [2, 1]


def test_bubbles():
  new_unsorted = UNSORTED[:]
  bubble_sort(new_unsorted, generate=False)
  assert new_unsorted == SORTED 


def test_insertion():
  new_unsorted = UNSORTED[:]
  insertion_sort(new_unsorted, generate=False)
  assert new_unsorted == SORTED 


def test_selection():
  new_sorted = UNSORTED[:]
  selection_sort(new_sorted, generate=False)
  assert new_sorted == SORTED


def test_merge():
  pass

