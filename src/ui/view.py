# import pygame
from src.algos import *

UNSORTED = [8, 2, 5, 9, 1, 4, 3, 5, 2]
SORTED =   [1, 2, 2, 3, 4, 5, 5, 8, 9]

def main():
  # bubble_sort(UNSORTED)
  # print(UNSORTED)

  # insertion_sort(UNSORTED)
  # print(UNSORTED)

  selection_sort(UNSORTED)
  print(UNSORTED)