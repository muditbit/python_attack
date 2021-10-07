import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide"
import sys, pygame
from pygame.locals import *

pygame.init()

width = 550
height = 300
color = (255,250,250)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pygame Bouncing Ball")

ball = pygame.image.load("ball.png")
rect_boundry = ball.get_rect()


speed = [3,3]


while 1:
    for event in pygame.event.get():
        rect_boundry = rect_boundry.move(speed)
        if rect_boundry.left<0 or rect_boundry.right>width:
            speed[0] = -speed[0]
        if rect_boundry.top<0 or rect_boundry.bottom > height:
            speed[1] = -speed[1]

            screen.fill(color)
            screen.blit(ball,rect_boundry)
            pygame.display.flip()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
