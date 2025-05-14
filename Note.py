import pygame
from collections import deque

class Note(pygame.sprite.Sprite):
  def __init__(self, type:int, pitch:int, note_height:int, primary_color:pygame.Color):
    super().__init__()
    self.type = type
    self.pitch = pitch
    self.note_height = note_height
    self.primary_color = primary_color
    self.image = self.create_note()
    return

  def create_note(self):
    # draw a whole note surface/image
    note_surface = pygame.Surface((int(self.note_height * 1.3), self.note_height))
    note_surface.set_colorkey("black")
    pygame.draw.ellipse(note_surface,  self.primary_color, (0, 0, int(self.note_height * 1.3), self.note_height))
    return note_surface

class NoteManager(pygame.sprite.Group):
  def __init__(self, background_surface, *sprites):
    super().__init__(*sprites)
    self.drawingScreen = background_surface
    self.clearingScreen = background_surface.copy()

  def draw(self, bgsurf = None, special_flags = 0):
    #print("drawing")
    return super().draw(self.drawingScreen, bgsurf, special_flags)
  
  def clear(self):
    #print("clearing")
    return super().clear(self.drawingScreen, self.clearingScreen)

  #sprites() returns a list of sprites in the group that you can modify the rects of.

class Melody(deque):
  def __init__(self, *notes:Note):
      super().__init__(notes)
  
  # wrap the queue methods!!

