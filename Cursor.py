import pygame
from Animation import Animation

class Cursor(pygame.sprite.Sprite):
  def __init__(self, list_of_images):
    super().__init__()
    
    self.image = list_of_images[0]
    self.rect = self.image.get_rect()
    self.animation = Animation(list_of_images)
  
  def update(self):
    self.image = self.animation.tick()

  def set_loc(self, location):
    self.rect.x = location[0]
    self.rect.y = location[1]

class CursorManager(pygame.sprite.GroupSingle):
  def __init__(self, background_surface:pygame.Surface, sprite=None):
    super().__init__(sprite=None)
    self.drawingScreen = background_surface
    self.clearingScreen = background_surface.copy()

  def draw(self, bgsurf = None, special_flags = 0):
    #print("drawing")
    return super().draw(self.drawingScreen, bgsurf, special_flags)
  
  def clear(self):
    #print("clearing")
    return super().clear(self.drawingScreen, self.clearingScreen)
