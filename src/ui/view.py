from src.algos import *
import pygame, sys
from src.ui.colors import *
from src.ui.gui import Text, Button, RadioButtons, OptionType


UNSORTED = [8, 2, 5, 9, 1, 4, 3, 5, 2]
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

  WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
  BACKGROUND = pygame.Rect(0, 0, WIDTH, HEIGHT)
  VISUAL_BOX = pygame.Rect(0, 200, WIDTH, HEIGHT - 200) 

  title = Text('Sorting Algo Visualizer', BLACK, 38)
  run_text = Text('Run', BLACK, 28)
  run_button = Button(1140, 60, run_text)
  radio_buttons = RadioButtons([OptionType(label='1'), OptionType(label='2')], initial_x=1000, initial_y=50)

  while run:
    clock.tick(FPS)
    check_events(run_button, radio_buttons)
    draw(WIN, BACKGROUND, VISUAL_BOX, title, run_button, radio_buttons)


def draw(WIN, BACKGROUND, VISUAL_BOX, title, run_button, radio):
  x, y = pygame.mouse.get_pos()

  pygame.draw.rect(WIN, WHITE, BACKGROUND)
  pygame.draw.rect(WIN, GRAY, VISUAL_BOX)
  
  title.render(WIN, WIDTH//2 - title.text_surface.get_width()//2, 10)
  run_button.draw_button(WIN=WIN, mouse_x=x, mouse_y=y, text_x_padding=20, text_y_padding=7)
  radio.draw_radio_buttons(WIN=WIN, mouse_x=x, mouse_y=y)
  pygame.display.update()


def check_events(run_button, radio_buttons):
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
        run_the_visualization(radio_buttons.selected)
      
      for i, button in enumerate(radio_buttons.buttons):
        if button.button.collidepoint(event.pos):
          radio_buttons.selected = i


def run_the_visualization(selected_index):
  if selected_index == 0:
    algo = 'bubble'
  elif selected_index == 1:
    algo = 'selection'
  else:
    algo = 'insertion'
  print(f'running visualization with algo: {algo}')