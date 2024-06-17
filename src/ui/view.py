from src.algos import *
import pygame, sys
from src.ui.colors import *
from src.ui.gui import Text, Button, RadioButtons, OptionType
from typing import List
import random

def randomize_list() -> List[int]:
  return [random.randint(1, 100) for i in range(138)]

unsorted_random = randomize_list()
unsorted = unsorted_random
WIDTH = 1280
HEIGHT = 720
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
sorting = False


class ButtonGroup:
  def __init__(self, run_button: Button, radio_buttons: RadioButtons, clear_button: Button, direction_buttons: RadioButtons):
    self.run_button = run_button
    self.radio_buttons = radio_buttons
    self.clear_button = clear_button
    self.direction_buttons = direction_buttons


class TextGroup:
  def __init__(self, title):
    self.title = title


class DrawGroup:
  def __init__(self, WIN, BACKGROUND, VISUAL_BOX, text_group: TextGroup, button_group: ButtonGroup):
    self.WIN = WIN
    self.BACKGROUND = BACKGROUND
    self.VISUAL_BOX = VISUAL_BOX

    self.title = text_group.title

    self.run_button = button_group.run_button
    self.radio_buttons = button_group.radio_buttons
    self.clear_button = button_group.clear_button
    self.direction_buttons = button_group.direction_buttons


def main():
  pygame.init()
  pygame.font.init()
  pygame.display.set_caption("Sorting Algo Visualizer")
  programIcon = pygame.image.load('assets/bee.jpg')
  pygame.display.set_icon(programIcon)
  clock = pygame.time.Clock()
  run = True
  visual_rects = initialize_visual_rects()
  
  BACKGROUND = pygame.Rect(0, 0, WIDTH, HEIGHT)
  VISUAL_BOX = pygame.Rect(0, 200, WIDTH, HEIGHT - 200) 

  title = Text('Sorting Algo Visualizer', BLACK, 38)
  run_text = Text('Run', BLACK, 50)
  run_button = Button(1140, 40, run_text)

  clear_text = Text('Clear', BLACK, 50)
  clear_button = Button(20, 40, clear_text, 100, 60, YELLOW)
  radio_buttons = RadioButtons([OptionType(label='Bubble sort'), 
                                OptionType(label='Insertion sort'),
                                # OptionType(label='Selection sort')
                                ], initial_x=950, initial_y=40)
  direction_buttons = RadioButtons([OptionType(label='ASC'),
                                    OptionType(label='DESC')],
                                    initial_x=800, initial_y=40)

  button_group = ButtonGroup(run_button, radio_buttons, clear_button, direction_buttons)
  text_group = TextGroup(title)
  draw_group = DrawGroup(WIN, BACKGROUND, VISUAL_BOX, text_group, button_group)
  while run:
    clock.tick(FPS)
    visual_rects = check_events(draw_group, visual_rects)
    draw(draw_group, visual_rects)


def draw(draw_group: DrawGroup, visual_rects: List[pygame.Rect], visual_rects_j=None, visual_rects_j_1=None):
  x, y = pygame.mouse.get_pos()

  pygame.draw.rect(draw_group.WIN, GRAY, draw_group.BACKGROUND)
  pygame.draw.rect(draw_group.WIN, GRAY, draw_group.VISUAL_BOX)
  
  draw_group.title.render(WIN, WIDTH//2 - draw_group.title.text_surface.get_width()//2, 10)
  draw_group.run_button.draw_button(WIN=WIN, mouse_x=x, mouse_y=y, text_x_padding=15, text_y_padding=10)
  draw_group.radio_buttons.draw_radio_buttons(WIN=WIN, mouse_x=x, mouse_y=y)

  draw_group.clear_button.draw_button(WIN=WIN, mouse_x=x, mouse_y=y, text_x_padding = 4, text_y_padding=10)
  draw_group.direction_buttons.draw_radio_buttons(WIN=WIN, mouse_x=x, mouse_y=y)

  draw_rects(visual_rects, visual_rects_j, visual_rects_j_1)
  pygame.display.update()


def check_events(draw_group, visual_rects):
  global unsorted

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit() 

    # key pressed
    if event.type == pygame.KEYDOWN:    
      pass  
      # if event.key == pygame.K_UP:
      #   print('up')
      # elif event.key == pygame.K_DOWN:
      #   print('down')
      # elif event.key == pygame.K_RIGHT:
      #   print('right')
      # elif event.key == pygame.K_LEFT:
      #   print('left')   

    if event.type == pygame.MOUSEBUTTONDOWN:
      if draw_group.run_button.button.collidepoint(event.pos):
        visual_rects = run_the_visualization(visual_rects, draw_group.radio_buttons.selected, draw_group)

      if draw_group.clear_button.button.collidepoint(event.pos):
        unsorted = randomize_list()
        visual_rects = initialize_visual_rects()
      
      for i, button in enumerate(draw_group.radio_buttons.buttons):
        if button.button.collidepoint(event.pos):
          draw_group.radio_buttons.selected = i

      for i, button in enumerate(draw_group.direction_buttons.buttons):
        if button.button.collidepoint(event.pos):
          draw_group.direction_buttons.selected = i
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


def run_the_visualization(visual_rects, selected_index, draw_group) -> List[pygame.Rect]:
  global sorting

  if selected_index in [0, 1, 2]:
    sorting = True

    if selected_index == 0:
      algo = bubble_sort
      
    elif selected_index == 1:
      algo = insertion_sort
     
    elif selected_index == 2:
      algo = selection_sort

    print(f'running visualization with algo: {algo}')
    direction = 'ASC'
    if draw_group.direction_buttons.selected == 0:
      direction = 'ASC'
    else:
      direction = 'DESC'

    # j = 0
    # j_1 = 0
    while sorting:
      try:
        # print(f'sorting {pygame.time.get_ticks()}')
        j, j_1 = next(algo(unsorted, direction, generate=True))
        print(j, j_1)
      except:
        sorting = False
      visual_rects = initialize_visual_rects()
      draw(draw_group, visual_rects, visual_rects_j=j, visual_rects_j_1=j_1)
      # print(unsorted)
      # pygame.time.delay(250)
      check_events(draw_group, visual_rects)
  return visual_rects


def draw_rects(visual_rects, visual_rects_j=None, visual_rects_j_1=None):
  for i, rect in enumerate(visual_rects):
    if i == visual_rects_j_1:
      pygame.draw.rect(WIN, GREEN, rect)
    else:
      pygame.draw.rect(WIN, RED, rect)


