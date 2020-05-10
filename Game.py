
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
  def getpower(self):
    return self.val

  def clear(self):
    val=0
  




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
    self.speed = 0
  def isteam1(self):
      return self.team==1
  def isteam2(self):
      return self.team==2
  def select(self):
      self.isselected=True
  def unselect(self):
      self.isselected=False
  def getangle(self):
      return angle
  def go(self, p, a):
      angle=a
      speed=p
    
      
    
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
pygame.display.set_caption("Fling Footie")#Title of Window
basicfont = pygame.font.SysFont(None, 48)
menufont = pygame.font.SysFont(None, 60)
powerfont = pygame.font.SysFont(None, 20)
controlsfont = pygame.font.SysFont(None, 30)
menutext = menufont.render('Fling Footie', True, (255, 255, 255), (86, 176, 17))
menurectangle = menutext.get_rect()
menurectangle.centerx = window.get_rect().centerx
menurectangle.top = 200
menudes = basicfont.render('Our Shuffle Board Soccer Mashup!', True, (255, 255, 255), (86, 176, 17))
menudesrectangle = menudes.get_rect()
menudesrectangle.centerx = window.get_rect().centerx
menudesrectangle.top =  275
i1= controlsfont.render('P to play', True, (0, 0, 0), (86, 176, 17))
i1r = i1.get_rect()
i1r.centerx = window.get_rect().centerx
i1r.top =  450
i2= controlsfont.render('I for instructions/rules', True, (0, 0, 0), (86, 176, 17))
i2r = i2.get_rect()
i2r.centerx = window.get_rect().centerx
i2r.top =  500
i3= controlsfont.render('Q to quit', True, (0, 0, 0), (86, 176, 17))
i3r = i3.get_rect()
i3r.centerx = window.get_rect().centerx
i3r.top =  550
i4= controlsfont.render('Press:', True, (0, 0, 0), (86, 176, 17))
i4r = i4.get_rect()
i4r.centerx = 300
i4r.top =  400
powertext = powerfont.render('Power Bar', True, (255,255,255), (0, 0, 0))
gametext = basicfont.render('London Derby(Emirates Stadium)', True, (255, 255, 255), (0, 0, 0))#Setting Title at top of Screen
gametextrectangle = gametext.get_rect()#Creating rectangle for text
gametextrectangle.centerx = window.get_rect().centerx
gametextrectangle.top = 40
dis = setupgame('Oliver')
powerbar = bar()
somethingselected=False
currentlyselected=player(1, 'rm')
turn = 1
running = True
state='menu'
while running:
  if(state=='menu'):
      window.fill((86,176,17))
      window.blit(menutext,menurectangle)
      window.blit(menudes,menudesrectangle)
      window.blit(i1,i1r)
      window.blit(i2,i2r)
      window.blit(i3,i3r)
      window.blit(i4,i4r)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:#add instructions
                running = False
            if event.key == pygame.K_p:#add instructions
                state='game'

      pygame.display.update()
      
  if(state=='game'):
      window.fill((0,0,0))
      window.blit(field, (0,129))
      window.blit(gametext, gametextrectangle)
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
            if event.key == pygame.K_SPACE:
                currentlyselected.go(power,angle)
                powerbar.clear()
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
