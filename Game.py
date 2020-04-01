import pygame
import time

class game:
  def __init__(self,nameOfPlayer):
    name=nameOfPlayer
    self.thingsToDisplay=[]
  def add(self,thing):
    self.thingsToDisplay.append(thing)


class ball:
  def __init__(self,still):
    self.piece = 'images/ball.png'
    self.piece = pygame.image.load(self.piece)
    self.piece = pygame.transform.scale(self.piece,(20,20))
    self.x = 390
    self.y = 390
    moving = not still



class player:
  def __init__(self,team,position):
    self.team = team
    if(team==1):
      self.piece='images/arsenal.png'
    if(team==2):
      self.piece='images/chelsea.png'
    if(position=='ST' and team==1):
        self.y = 375
        self.x = 450
    if(position=='ST' and team==2):
        self.y = 375
        self.x = 300
    if(position=='LM' and team==1):
        self.y = 480
        self.x = 550
    if(position=='LM' and team==2):
        self.y = 270
        self.x = 195
    if(position=='RM' and team==1):
        self.y = 270
        self.x = 550
    if(position=='RM' and team==2):
        self.y = 480
        self.x = 195
    if(position=='CB' and team==1):
        self.y = 375
        self.x = 665
    if(position=='CB' and team==2):
        self.y = 375
        self.x = 80
    self.piece = pygame.image.load(self.piece)
    self.piece = pygame.transform.scale(self.piece,(50,50))
    
      
    
def setupgame(name):#sets up the game
  currentgame = game(name)
  gameball = ball(True)
  st1 = player(1,'ST')
  st2 = player(2,'ST')
  lm1 = player(1,'LM')
  lm2 = player(2,'LM')
  rm1 = player(1,'RM')
  rm2 = player(2,'RM')
  cb1 = player(1,'CB')
  cb2 = player(2,'CB')
  currentgame.add(gameball)
  currentgame.add(st1)
  currentgame.add(st2)
  currentgame.add(lm1)
  currentgame.add(lm2)
  currentgame.add(rm1)
  currentgame.add(rm2)
  currentgame.add(cb1)
  currentgame.add(cb2)
  
  return currentgame.thingsToDisplay
  
  
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
dis = setupgame('Oliver')

running = True
while running:
  window.fill((0,0,0))
  window.blit(field, (0,129))
  window.blit(text, textrectangle)
  for o in dis:
      window.blit(o.piece,(o.x,o.y))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    pygame.display.update()



pygame.quit()
