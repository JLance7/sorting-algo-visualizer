import pygame
from src.ui.colors import *
from typing import List

class Text():
  def __init__(self, text='', color=BLACK, font_size=20, font='Comic Sans'):
    self.font = pygame.font.SysFont(font, font_size)
    self.color = color
    self.text = text
    self.text_surface = self.font.render(self.text, True, self.color)

  
  def render(self, blit_obj, x, y):
    blit_obj.blit(self.text_surface, (x, y))


class Button():
  def __init__(self, x, y, text_obj=None, width=100, height=60, color=GREEN, hover_color=BLUE):
    self.width = width
    self.height = height
    self.button = pygame.Rect(x, y, width, height)
    self.text_obj = text_obj
    self.color = color
    self.hover_color = hover_color

  def check_mouse_collides(self, mouse_x, mouse_y) -> bool:
    if (self.button.x <= mouse_x <= self.button.x + self.width) and (self.button.y <= mouse_y <= self.button.y + self.height):
      return True
    else:
      return False
    
  def draw_button(self, WIN, mouse_x, mouse_y, text_x_padding=0, text_y_padding=0):
    if self.check_mouse_collides(mouse_x, mouse_y):
      pygame.draw.rect(WIN, self.hover_color, self.button)
    else:
      pygame.draw.rect(WIN, self.color, self.button)
    
    if self.text_obj != None:
      self.text_obj.render(WIN, self.button.x + text_x_padding, self.button.y + text_y_padding)


class RadioButton(Button):
  def __init__(self, options: List[str], x, y, text_obj=None, width=100, height=60, color=GREEN, hover_color=BLUE):
    self.options = options
    super().__init__(x, y, text_obj, width, height, color, hover_color)

  def draw_radio_button(self, mouse_x, mouse_y):
    if self.check_mouse_collides(mouse_x, mouse_y):
      pass
    else:
      pass
