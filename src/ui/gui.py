from dataclasses import dataclass
import pygame
from src.ui.colors import *
from typing import List, Dict


@dataclass
class OptionType:
  label: str


class Text():
  def __init__(self, text='', color=BLACK, font_size=20, font='Comic Sans'):
    self.font = pygame.font.SysFont(font, font_size)
    self.color = color
    self.text = text
    self.text_surface = self.font.render(self.text, True, self.color)

  def render(self, blit_obj, x, y):
    blit_obj.blit(self.text_surface, (x, y))


class Button():
  def __init__(self, x, y, text_obj=None, width=100, height=60, color=GREEN, hover_color=BLUE, transparent=False):
    self.width = width
    self.height = height
    self.button = pygame.Rect(x, y, width, height)
    self.text_obj = text_obj
    self.color = color
    self.hover_color = hover_color
    self.transparent = transparent

  def check_mouse_collides(self, mouse_x, mouse_y) -> bool:
    if (self.button.x <= mouse_x <= self.button.x + self.width) and (self.button.y <= mouse_y <= self.button.y + self.height):
      return True
    else:
      return False
    
  def draw_button(self, WIN, mouse_x, mouse_y, text_x_padding=0, text_y_padding=0):
    if not self.transparent:
      if self.check_mouse_collides(mouse_x, mouse_y):
        pygame.draw.rect(WIN, self.hover_color, self.button)
      else:
        pygame.draw.rect(WIN, self.color, self.button)
      
    if self.text_obj != None:
      self.text_obj.render(WIN, self.button.x + text_x_padding, self.button.y + text_y_padding)


class RadioButtons():
  def __init__(self, options: List[OptionType], initial_x, initial_y):
    self.options = options
    self.selected = 0
    self.buttons: List[Button] = []

    for x in options:
      text = Text(x.label, BLACK, 28)
      my_button = Button(initial_x, initial_y, text, 50, 30, None, None, transparent=True)
      self.buttons.append(my_button) # type: ignore
      initial_y += 45

  def draw_radio_buttons(self, WIN, mouse_x, mouse_y):
    for i, button in enumerate(self.buttons):
      if i == self.selected:
        pygame.draw.circle(WIN, RED, (button.button.x, button.button.y + 10), 10)
      else:
        pygame.draw.circle(WIN, BLUE, (button.button.x, button.button.y + 10), 10)

      if button.text_obj != None:
        button.text_obj.render(WIN, button.button.x + 15, button.button.y + 2)
