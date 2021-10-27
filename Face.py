import pygame
from pygame.draw import *
pygame.init()

X, Y = 600, 400
screen = pygame.display.set_mode((X, Y))
rect(screen, (255, 255, 224), (0,0,X,Y))

circle(screen, (255, 255, 0), (300,200), 150)
rect(screen, (0, 0, 0), (220,270,160,30))

circle(screen, (255, 0, 0), (240,180), 40)
circle(screen, (0, 0, 0), (240,180), 40, 4)
circle(screen, (255, 0, 0), (360,180), 30)
circle(screen, (0, 0, 0), (360,180), 30, 4)

circle(screen, (0, 0, 0), (240,180), 10)
circle(screen, (0, 0, 0), (360,180), 10)

line(screen, (0,0,0), (290,160), (180,110), 20)
line(screen, (0,0,0), (310,160), (420,140), 20)



pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
