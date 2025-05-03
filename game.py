# Example file showing a circle moving on screen
import pygame
from Stave import *
from Cursor import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# We can draw the staff once
# draw the staff (stave_line_thickness lines)
# need surface to draw on
background_color = "lemonchiffon1"
primary_color = "lightsteelblue4"
screen.fill(background_color)
stave_offset = 30
stave_line_thickness = 4
padding = int(screen.get_width() * .1)

stave = Stave(screen, padding, 20, stave_offset, stave_line_thickness)

stave.randomize_notes()
stave.draw_notes()
stave.draw_stave(screen, primary_color)

# init cursor and its animation
cursor = Cursor(primary_color)

# we use the sprite group.draw, not the surface.blit to move the sprite (both works)
# GroupSingle because if we add a new image (surface), it deletes the old one, meaning we can add custom cursors.
# so you want to modify the rect to move, and .draw to render
cursor_manager = CursorManager(screen)
cursor_manager.add(cursor)
cursor.set_loc((stave.note_x_val() + 5,200))
cursor_manager.draw()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.TEXTINPUT:
            print("increment note")
            print(cursor.rect)
            stave.next_note()
            stave.cursor_to_note(cursor)
    
    cursor_manager.update()
    """ 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        """
    
    # draw/render changes below
    cursor_manager.clear()
    cursor_manager.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()