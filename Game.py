import pygame
import time


pygame.init()
pygame.font.init()

(width, height) = (800, 800)#Dimensions of Window

window = pygame.display.set_mode((width, height))

field = pygame.image.load('images/field.jpg')
field = pygame.transform.scale(field,(800,542))
pygame.display.set_caption("Soccer Game")#Title of Window
basicfont = pygame.font.SysFont(None, 48)
text = basicfont.render('Soccer Game', True, (255, 255, 255), (0, 0, 0))#Setting Title at top of Screen
textrectangle = text.get_rect()#Creating rectangle for text
textrectangle.centerx = window.get_rect().centerx
textrectangle.top = 40

running = True
while running:
  window.fill((0,0,0))
  window.blit(field, (0,129))
  window.blit(text, textrectangle)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    pygame.display.update()



pygame.quit()
