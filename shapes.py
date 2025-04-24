import pygame

def draw_note(surface:pygame.Surface, color:pygame.Color, rect:pygame.Rect, background_color:pygame.Color):
  # draw a whole note
  rect.scale_by_ip(.95)
  rect.top = int(rect.top + rect.height * .05)
  pygame.draw.ellipse(surface, color, rect)
  in_width = rect.width // 3
  in_height = rect.height - int(rect.height * .2)
  in_left = rect.midleft[0] + in_width
  in_top = rect.top + int(rect.height * .1)
  in_rect = pygame.Rect(in_left, in_top, in_width, in_height)
  pygame.draw.ellipse(surface, color, rect)
  pygame.draw.ellipse(surface, background_color, in_rect)
  #pygame.draw.line(surface, background_color, rect.midtop, rect.midbottom, rect.width // 3)


class Stave:
  def __init__(self, screen, padding, note_margin, stave_offset, stave_line_thickness):
    self.screen = screen

    self.stave_offset = stave_offset
    self.stave_line_thickness = stave_line_thickness

    self.note_margin = note_margin
    self.note_height = stave_offset
    self.note_width = int(self.note_height * 1.3)

    self.padding = padding
    self.stave_width = int(screen.get_width() - 2 * padding)
    self.bottom_line_y = int(screen.get_height() / 2 + 2 * self.stave_offset)
    
    self.note_list = [-1] * int(self.stave_width / (self.note_width + self.note_margin))
  
  def get_notes(self):
    return self.note_list
  
  notes = property(get_notes)


  def draw_stave(self, screen:pygame.Surface, primary_color:pygame.Color):
    width = screen.get_width()
    pygame.draw.line(screen, primary_color, (self.padding, self.bottom_line_y + -4 * self.stave_offset), (width - self.padding,  self.bottom_line_y + -4 * self.stave_offset), self.stave_line_thickness)
    pygame.draw.line(screen, primary_color, (self.padding, self.bottom_line_y + -3 * self.stave_offset), (width - self.padding,  self.bottom_line_y + -3 * self.stave_offset), self.stave_line_thickness)
    pygame.draw.line(screen, primary_color, (self.padding, self.bottom_line_y + -2 * self.stave_offset), (width - self.padding, self.bottom_line_y + -2 * self.stave_offset), self.stave_line_thickness)
    pygame.draw.line(screen, primary_color, (self.padding, self.bottom_line_y + -1 * self.stave_offset), (width - self.padding,  self.bottom_line_y + -1 * self.stave_offset), self.stave_line_thickness)
    pygame.draw.line(screen, primary_color, (self.padding, self.bottom_line_y + 0 * self.stave_offset), (width - self.padding,  self.bottom_line_y + 0 * self.stave_offset), self.stave_line_thickness)
    return
  
  def draw_notes(self):

    # example_rect = pygame.Rect(100, middle + 1 * stave_offset, int(note_height * 1.3), note_height)
    # draw_note(screen, primary_color, example_rect, background_color)
    self.bottom_space = self.bottom_line_y + int(.5 * self.stave_offset)
    

    # padding + i * (self.note_width + self.note_margin)
    for i in range(len(self.notes)):
      rect =  pygame.Rect(self.padding + i * (self.note_width + self.note_margin), self.notes[i] * -0.5 * self.stave_offset +  self.bottom_line_y, self.note_width, self.note_height)
      draw_note(self.screen, "lightsteelblue4", rect, "lemonchiffon1")  
