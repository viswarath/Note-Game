import pygame

class Animation:
  def __init__(self, list_of_images):
    self.images = list_of_images
    self.max_index = len(list_of_images) - 1
    self.index = 0
    self.ticks = 0
  
  def tick(self):
    self.ticks += 1
    if self.ticks == 60:
      self.ticks = 0

    self.index = self.ticks // 30

    return self.images[self.index]