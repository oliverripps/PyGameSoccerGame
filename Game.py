
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
    self.isselected=False
    self.piece = 'images/ball.png'
    self.piece = pygame.image.load(self.piece)
    self.piece = pygame.transform.scale(self.piece,(20,20))
    self.x = 390
    self.angle=0
    self.y = 390
    self.moving = not still

class bar:
  def __init__(self):
    self.color = (0,0,0)
    self.value=0
    self.x = 750
    self.y = 120
  def add(self):
    if(self.value<8):
        self.setvalue(self.value+1)
  def minus(self):
    if(self.value>0):
        self.setvalue(self.value-1)  
  def setvalue(self,val):
    self.value=val
    if(val==0):
        self.color = (0,0,0)
    if(val==1 or val ==2):
        self.color = (0,128,0)
    if(val==3 or val ==4):
        self.color = (255,255,0)
    if(val==5 or val ==6):
        self.color = (255,165,0)
    if(val==7 and val ==8):
        self.color = (255,0,0)




class player:
  def __init__(self,team,position):
    self.team = team
    self.isselected=False
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
    self.angle = 0
    self.piece = pygame.image.load(self.piece)
    self.piece = pygame.transform.scale(self.piece,(50,50))
  def isteam1(self):
      return self.team==1
  def isteam2(self):
      return self.team==2
  def select(self):
      self.isselected=True
  def unselect(self):
      self.isselected=False

    
      
    
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
powerfont = pygame.font.SysFont(None, 20)
powertext = powerfont.render('Power Bar', True, (255,255,255), (0, 0, 0))
text = basicfont.render('Soccer Game', True, (255, 255, 255), (0, 0, 0))#Setting Title at top of Screen
textrectangle = text.get_rect()#Creating rectangle for text
textrectangle.centerx = window.get_rect().centerx
textrectangle.top = 40
dis = setupgame('Oliver')
powerbar = bar()
somethingselected=False
currentlyselected=player(1, 'rm')
turn = 1
running = True
state='game'
while running:
  if(state=='game'):
      window.fill((0,0,0))
      window.blit(field, (0,129))
      window.blit(text, textrectangle)
      window.blit(powertext,(725,20))
      powerrect = pygame.Rect(powerbar.x,powerbar.y,15,powerbar.value*-10)
      pygame.draw.rect(window,powerbar.color,powerrect)
      ev = pygame.event.get()
      for o in dis:
          window.blit(o.piece,(o.x,o.y))
          if (o.isselected):
              pygame.draw.circle(window,(255,255,0),(o.x+25,o.y+25),26,2)
      for event in pygame.event.get():
      
        if event.type == pygame.MOUSEBUTTONUP:
          pos = pygame.mouse.get_pos()
          for o in dis:
              xdif = pos[0]-o.x
              ydif = pos[1]-o.y
              if xdif > -50 and xdif<50 and ydif > -50 and ydif < 50 and o.team==turn:
                  old = currentlyselected
                  currentlyselected = o
                  old.unselect()
                  o.select()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:#add instructions
                running = False
            if event.key == pygame.K_w:#add instructions
                powerbar.add()
            if event.key == pygame.K_s:#add instructions
                powerbar.minus()
            #next steps
            #USE BRANCHES!!!!!! everyone make a branch
            #will-angle arrow thing
            #oliver-space bar applies power and angle
            #ryan-x value and y value
                #x+=(cos(angle))
                #y+=(sin(angle))
            #nic-ball/peice collisions(direct, power, angles...)
                #be the hardest so prob need all of us
            #oliver
            #levels and losing/winning(scoreboard--turns/goals/level number)
            #menu screen easy medium hard
            #
            
        pygame.display.update()


pygame.quit()
