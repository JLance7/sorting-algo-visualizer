from src.algos import *
import pygame, sys
from src.ui.colors import *
from src.ui.gui import Text, Button, RadioButtons, OptionType
from typing import List
import random

unsorted_random = [random.randint(1, 100) for i in range(138)]
print(unsorted_random)
unsorted = unsorted_random
SORTED =   [1, 2, 2, 3, 4, 5, 5, 8, 9]
WIDTH = 1280
HEIGHT = 720
FPS = 60


def main():
  pygame.init()
  pygame.font.init()
  pygame.display.set_caption("Sorting Algo Visualizer")
  programIcon = pygame.image.load('assets/bee.jpg')
  pygame.display.set_icon(programIcon)
  clock = pygame.time.Clock()
  run = True
  visual_rects = initialize_visual_rects()

  WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
  BACKGROUND = pygame.Rect(0, 0, WIDTH, HEIGHT)
  VISUAL_BOX = pygame.Rect(0, 200, WIDTH, HEIGHT - 200) 

  title = Text('Sorting Algo Visualizer', BLACK, 38)
  run_text = Text('Run', BLACK, 28)
  run_button = Button(1140, 60, run_text)
  radio_buttons = RadioButtons([OptionType(label='Bubble sort'), 
                                OptionType(label='Insertion sort'),
                                OptionType(label='Selection sort')
                                ], initial_x=1000, initial_y=50)

  while run:
    clock.tick(FPS)
    visual_rects = check_events(visual_rects, run_button, radio_buttons)
    draw(WIN, BACKGROUND, VISUAL_BOX, title, run_button, radio_buttons, visual_rects)


def draw(WIN, BACKGROUND, VISUAL_BOX, title, run_button, radio, visual_rects):
  x, y = pygame.mouse.get_pos()

  pygame.draw.rect(WIN, GRAY, BACKGROUND)
  pygame.draw.rect(WIN, GRAY, VISUAL_BOX)
  
  title.render(WIN, WIDTH//2 - title.text_surface.get_width()//2, 10)
  run_button.draw_button(WIN=WIN, mouse_x=x, mouse_y=y, text_x_padding=20, text_y_padding=7)
  radio.draw_radio_buttons(WIN=WIN, mouse_x=x, mouse_y=y)

  for rect in visual_rects:
    pygame.draw.rect(WIN, RED, rect)
  pygame.display.update()


def check_events(visual_rects, run_button, radio_buttons):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit() 

    # key pressed
    if event.type == pygame.KEYDOWN:      
      if event.key == pygame.K_UP:
        print('up')
      elif event.key == pygame.K_DOWN:
        print('down')
      elif event.key == pygame.K_RIGHT:
        print('right')
      elif event.key == pygame.K_LEFT:
        print('left')   

    if event.type == pygame.MOUSEBUTTONDOWN:
      if run_button.button.collidepoint(event.pos):
        visual_rects = run_the_visualization(visual_rects, radio_buttons.selected)
      
      for i, button in enumerate(radio_buttons.buttons):
        if button.button.collidepoint(event.pos):
          radio_buttons.selected = i
  return visual_rects


def initialize_visual_rects() -> List[pygame.Rect]:
  x = 20
  y = 720
  visual_rects = []
  for i in range(len(unsorted)):
    rect_height = unsorted[i] * 5
    rect_y_start = y - rect_height
    rect = pygame.Rect(x, rect_y_start, 8, rect_height)
    visual_rects.append(rect)
    x += 9
  return visual_rects


def run_the_visualization(visual_rects, selected_index) -> List[pygame.Rect]:
  if selected_index == 0:
    algo = 'bubble'
    print(f'running visualization with algo: {algo}')
    bubble_sort(unsorted)
    visual_rects = initialize_visual_rects()
  elif selected_index == 1:
    algo = 'insertion'
    print(f'running visualization with algo: {algo}')
    insertion_sort(unsorted)
    visual_rects = initialize_visual_rects()
  else:
    algo = 'selection'
    print(f'running visualization with algo: {algo}')
    selection_sort(unsorted)
    visual_rects = initialize_visual_rects()
  return visual_rects


if __name__ == "__main__":
  run_the_visualization(None, 0)