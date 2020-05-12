import random
import pygame
import time
import math

class game:
  def __init__(self):
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
    self.team=3
    self.moving = not still
    self.deltax=0
    self.deltay=0

  def move(self):
    if(self.deltax != 0 or self.deltay != 0):
      if self.deltax > 2 or self.deltax < -2:
        self.deltax *= .95
        
        self.x += int(self.deltax)
        if self.x<60:#fix for left bound
          if self.y>350 and self.y< 450:#fi
            reset(turn)
          else:
            self.deltax*=-1
            self.x+=20
            
        if self.x>740:#fix for right bound
          if self.y>350 and self.y< 450:#fi
            reset(turn)
          else:
            self.deltax*=-1
            self.x-=20

        if self.deltax < 2 and self.deltax >-2:
          self.deltax=0
          
      if self.deltay > 2 or self.deltay < -2:
        self.deltay *= .95
        print("deltay:")
        print(self.deltay)
        self.y -= int(self.deltay)
        if self.y<200:#fix for upper bound
          self.deltay*=-1
          
            
        if self.y>600:#fix for lower bound
          print("too low")
          print(self.deltay)
          self.deltay=self.deltay *-1
          print(self.deltay)
          #self.y-=100

        if self.deltay < 2 and self.deltay >-2:
          self.deltax=0
      
      else:
        if self in moving:
          moving.remove(self)
        
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
    if(val==7 or val ==8):
        self.color = (255,0,0)
  def getpower(self):
    return self.value

  def clear(self):
    self.value=0
    self.color = (0,0,0)
  




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
    self.deltax=0
    self.deltay=0
    
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
      self.angle=a
      self.speed=p
  
  def move(self):
    if(self.deltax != 0 or self.deltay != 0):
      if self.deltax > 2 or self.deltax < -2:
        self.deltax *= .95
        
        self.x += int(self.deltax)
        if self.x<50:#fix for left bound
          self.deltax*=-1
          self.x+=(self.deltax/.9)
          self.deltax*=.75
          self.deltay*=.75
        if self.x>700:#fix for right bound
          self.deltax*=-1
          self.x+=(self.deltax/.9)
          self.deltax*=.75
          self.deltay*=.75
        if self.deltax < 2 and self.deltax >-2:
          self.deltax=0
          
      if self.deltay > 2 or self.deltay < -2:
        self.deltay *= .95
        self.y -= int(self.deltay)
        if self.y<150:#fix for upper bound
          self.deltay*=-1
          self.y-= (self.deltay/.9)
          self.deltay*=.75
          self.deltax*=.75
        if self.y>600:#fix for lower bound
          self.deltay=self.deltay *-1
          self.y-= (self.deltay/.9)
          self.deltay*=.75
          self.deltax*=.75
        if self.deltay < 2 and self.deltay >-2:
          self.deltax=0
      
      else:
        if self in moving:
          moving.remove(self)
        
      
    
def setupgame():#sets up the game
  currentgame = game()
  st1 = player(1,'ST')
  st2 = player(2,'ST')
  lm1 = player(1,'LM')
  lm2 = player(2,'LM')
  rm1 = player(1,'RM')
  rm2 = player(2,'RM')
  cb1 = player(1,'CB')
  cb2 = player(2,'CB')
  currentgame.add(st1)
  currentgame.add(st2)
  currentgame.add(lm1)
  currentgame.add(lm2)
  currentgame.add(rm1)
  currentgame.add(rm2)
  currentgame.add(cb1)
  currentgame.add(cb2)
  
  
  return currentgame.thingsToDisplay
  
def reset(team):
  dis=setupgame()
  if team==1:
    team2score+=1
  if team==2:
    team1score+=1
  if team1score==7 or team2score==7:
    state='over'

def reset():
  dis=setupgame()
  team1score=0
  team2score=0
  state='game'
def changeturn(v):
  if(v==1):
    return 2
  if(v==2):
    return 1
  
def getDistance(x1, y1, x2, y2):#https://www.pygame.org/wiki/CalculateDist
    deltay = y2 - y1
    deltax = x2 - x1
    return math.sqrt(math.pow(deltax, 2) + math.pow(deltay, 2))

        

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
r1= controlsfont.render('instructions', True, (255, 255, 255), (0, 0, 0))
r1r = r1.get_rect()
r1r.centerx = window.get_rect().centerx
r1r.top = 400
r2= controlsfont.render('Buttons to press', True, (255, 255, 255), (0, 0, 0))
r2r = r2.get_rect()
r2r.centerx = window.get_rect().centerx
r2r.top =  450
r3= controlsfont.render('At anytime press I for instructions or Q to quit', True, (255, 255, 255), (0, 0, 0))
r3r = r3.get_rect()
r3r.centerx = window.get_rect().centerx
r3r.top =  500
r4= basicfont.render('How To Play', True, (255, 255, 255), (0, 0, 0))
r4r = r4.get_rect()
r4r.centerx = window.get_rect().centerx
r4r.top =  200
g1= controlsfont.render('Press I for instructions or Q to quit', True, (255, 255, 255), (0, 0, 0))
g1r = g1.get_rect()
g1r.centerx = window.get_rect().centerx
g1r.top = 700
powertext = powerfont.render('Power Bar', True, (255,255,255), (0, 0, 0))
gametext = basicfont.render('London Derby(Emirates Stadium)', True, (255, 255, 255), (0, 0, 0))#Setting Title at top of Screen
gametextrectangle = gametext.get_rect()#Creating rectangle for text
gametextrectangle.centerx = window.get_rect().centerx
gametextrectangle.top = 40
team2score=0
team1score=0
dis = setupgame()
moving = []
powerbar = bar()
somethingselected=False
currentlyselected=player(1, 'rm')
t=0
turn = 1
angle=0
running = True
state='menu'
gameball = ball(True)
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
            if event.key == pygame.K_i:#add instructions
                state='instructions'
            

      pygame.display.update()
  if(state=='instructions'):
      window.fill((0,0,0))
      window.blit(r1,r1r)
      window.blit(r2,r2r)
      window.blit(r3,r3r)
      window.blit(r4,r4r)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:#add instructions
                running = False
            if event.key == pygame.K_p:#add instructions
                state='game'
            if event.key == pygame.K_m:#add instructions
                state='menu'
            

      pygame.display.update()
      
  if(state=='game'):
      scoretext = menufont.render("%s" % team2score, True, (255, 255, 255), (0, 0, 0))#
      sctr = scoretext.get_rect()#Creating rectangle for text
      sctr.centerx = 250
      sctr.top = 85
      scoretext2 = menufont.render("%s" % team1score, True, (255, 255, 255), (0, 0, 0))#
      sctr2 = scoretext2.get_rect()#Creating rectangle for text
      sctr2.centerx = 550
      sctr2.top = 85
      window.fill((0,0,0))
      window.blit(field, (0,129))
      window.blit(gametext, gametextrectangle)
      window.blit(powertext,(725,20))
      window.blit(scoretext,sctr)
      window.blit(scoretext2,sctr2)
      powerrect = pygame.Rect(powerbar.x,powerbar.y,15,powerbar.value*-10)
      pygame.draw.rect(window,powerbar.color,powerrect)
      window.blit(g1,g1r)
      for o in dis:
        window.blit(o.piece,(o.x,o.y))
        o.move()
        if (o.isselected):
          pygame.draw.circle(window,(255,255,0),(int(o.x)+25,int(o.y)+25),26,2)
      gameball.move()
      window.blit(gameball.piece,(gameball.x,gameball.y))
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
                angle= random.randint(1, 5)#NEEDS ANGLE
                currpow = powerbar.getpower()
                currpow*=8
                currentlyselected.deltax = currpow * math.cos(angle)
                currentlyselected.deltay = currpow * math.sin(angle)
                powerbar.clear()
                moving.append(currentlyselected)
                turn=changeturn(turn)
                currentlyselected.isselected=False
                currentlyselected=player(1, 'rm')

      pygame.display.update()  
  if(state=='over'):
      window.fill((0,0,0))
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:#add instructions
                running = False
            if event.key == pygame.k_a:
                reset()
            
      pygame.display.update()
    

pygame.quit()
