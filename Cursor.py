import pygame
from Animation import Animation

class Cursor(pygame.sprite.Sprite):
  def __init__(self, primary_color:pygame.Color):
    super().__init__()
    # make a sprite for the hovering "v"
    # need a surface to set the image of the sprite, and a rect

    # base surface for all animations of the cursor
    cursor_base = pygame.Surface((20,30))
    cursor_base.set_colorkey("black")

    cursor_0 = cursor_base.copy()
    # draw onto new surface
    pygame.draw.line(cursor_0, primary_color, (5,5), (10,20), 4)
    pygame.draw.line(cursor_0, primary_color, (10,20), (15,5), 4)

    cursor_1= cursor_base.copy()

    pygame.draw.line(cursor_1, primary_color, (5,10), (10,25), 4)
    pygame.draw.line(cursor_1, primary_color, (10,25), (15,10), 4)

    self.image = cursor_0
    self.rect = self.image.get_rect()
    self.animation = Animation([cursor_0, cursor_1])
  
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
