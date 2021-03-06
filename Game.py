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
    self.angle=0
    self.speed=0
    self.x = 390
    self.y = 390
    self.team=3
    self.moving = not still
    self.deltax=0
    self.deltay=0
    self.centerx = self.x + 10
    self.centery = self.y + 10
    self.hittime = 80

  def move(self):
    if(self.deltax != 0 or self.deltay != 0):
      if self.deltax > 2.5 or self.deltax < -2.5:
        self.deltax *= .98

        self.x += int(self.deltax)
        if self.x<60:#fix for left bound
          if self.y>350 and self.y< 450:#fi
            return turn
          else:
            self.deltax*=-1
            self.x+=20
            self.centerx = self.x + 10

        if self.x>740:#fix for right bound
          if self.y>350 and self.y< 450:#fi
            return turn
          else:
            self.deltax*=-1
            self.x-=20
            self.centerx = self.x + 10

        if self.deltax < 2.5 and self.deltax >-2.5:
          self.deltax=0

      if self.deltay > 2.5 or self.deltay < -2.5:
        self.deltay *= .98
        self.y -= int(self.deltay)
        self.centery = self.y + 10
        if self.y<200:#fix for upper bound
          self.deltay*=-1


        if self.y>600:#fix for lower boun
          self.deltay=self.deltay *-1
          #self.y-=100

        if self.deltay < 2.5 and self.deltay >-2.5:
          self.deltax=0

    return 0

    
class bar:
  def __init__(self):
    self.color = (0,0,0)
    self.value=0
    self.x = 750
    self.y = 120
    self.team = 3
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
    self.speed=0
    self.angle=0
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
    self.piece = pygame.image.load(self.piece)
    self.piece = pygame.transform.scale(self.piece,(50,50))
    self.deltax=0
    self.deltay=0
    self.hittime = 80
    if (position != 'rm'):
        self.centerx = self.x + 25
        self.centery = self.x + 25

  def isteam1(self):
      return self.team==1
  def isteam2(self):
      return self.team==2
  def select(self):
      self.isselected=True
  def unselect(self):
      self.isselected=False
  def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed

  def getangle(self):
      return angle
  def go(self, p, a):
      self.angle=a
      self.speed=p
  def pos(self):
    return (self.x+25, self.y+25)
  def getX(self):
    return self.x+25
  def getY(self):
    return self.y+25

  def move(self):
    if(self.deltax != 0 or self.deltay != 0):
      if self.deltax > 2 or self.deltax < -2:
        self.deltax *= .99

        self.x += int(self.deltax)
        if self.x<50:#fix for left bound
          self.deltax*=-1
          self.x+=(self.deltax/.9)
          self.centerx = self.x + 25
          #self.deltax*=.75
          #self.deltay*=.75
        if self.x>700:#fix for right bound
          self.deltax*=-1
          self.x+=(self.deltax/.9)
          self.centerx = self.x + 25
          #self.deltax*=.75
          #self.deltay*=.75
        if self.deltax < 2 and self.deltax >-2:
          self.deltax=0

      if self.deltay > 2 or self.deltay < -2:
        self.deltay *= .99
        self.y -= int(self.deltay)
        if self.y<150:#fix for upper bound
          self.deltay*=-1
          self.y-= (self.deltay/.9)
          self.centery = self.y + 25
          #self.deltay*=.75
          #self.deltax*=.75
        if self.y>600:#fix for lower bound
          self.deltay=self.deltay *-1
          self.y-= (self.deltay/.9)
          self.centery = self.y + 25
          #self.deltay*=.75
          #self.deltax*=.75
        if self.deltay < 2 and self.deltay >-2:
          self.deltax=0

      else:
        if self in moving:
          moving.remove(self)

def draw_line(player, angle, line_length):
  pos2 = (player.getX() + line_length*math.cos(angle),player.getY() + line_length*(-1*math.sin(angle)))
  pygame.draw.line(window, (0,0,0), player.pos(), pos2, 5)

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


def changeturn(v):
  if(v==1):
    return 2
  if(v==2):
    return 1

def getDistance(x1, y1, x2, y2):#https://www.pygame.org/wiki/CalculateDist
    deltay = y2 - y1
    deltax = x2 - x1
    return math.sqrt(math.pow(deltax, 2) + math.pow(deltay, 2))

def playerCollision(Ball1, Ball2):
    Ball1.hittime = 0
    Ball2.hittime = 0
    BallAngle = -math.atan2((Ball2.centery - Ball1.centery), (Ball2.centerx - Ball1.centerx))
    deltaVelocityX = Ball1.deltax - Ball2.deltax
    deltaVelocityY = Ball1.deltay - Ball2.deltay

    Ball1InitialVelocityX = (Ball1.deltax * math.cos(BallAngle)) - (Ball1.deltay * math.sin(BallAngle))
    Ball1InitialVelocityY = (Ball1.deltax * math.sin(BallAngle)) + (Ball1.deltay * math.cos(BallAngle))
    Ball2InitialVelocityX = (Ball2.deltax * math.cos(BallAngle)) - (Ball2.deltay * math.sin(BallAngle))
    Ball2InitialVelocityY = (Ball2.deltax * math.sin(BallAngle)) + (Ball2.deltay * math.cos(BallAngle))

    Ball1VelocityAfterCollisionX = Ball2InitialVelocityX * 2 * 10 / 20
    Ball1VelocityAfterCollisionY = Ball1InitialVelocityY
    Ball2VelocityAfterCollisionX = Ball1InitialVelocityX * 2 * 10 / 20
    Ball2VelocityAfterCollisionY = Ball2InitialVelocityY

    Ball1.deltax = (Ball1VelocityAfterCollisionX * math.cos(BallAngle)) - (Ball1VelocityAfterCollisionY * math.sin(BallAngle))
    Ball1.deltay = (Ball1VelocityAfterCollisionX * math.sin(BallAngle)) + (Ball1VelocityAfterCollisionY * math.cos(BallAngle))
    Ball2.deltax = (Ball2VelocityAfterCollisionX * math.cos(BallAngle)) - (Ball2VelocityAfterCollisionY * math.sin(BallAngle))
    Ball2.deltay = (Ball2VelocityAfterCollisionX * math.sin(BallAngle)) + (Ball2VelocityAfterCollisionY * math.cos(BallAngle))



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
r1= controlsfont.render('The game is taken in turns, starting with Arsenal.', True, (255, 255, 255), (0, 0, 0))
r1r = r1.get_rect()
r1r.centerx = window.get_rect().centerx
r1r.top = 300
r2= controlsfont.render('Click on a player and adjust the angle with A and D.', True, (255, 255, 255), (0, 0, 0))
r2r = r2.get_rect()
r2r.centerx = window.get_rect().centerx
r2r.top =  350
r3= controlsfont.render('Press W to increase the power and S to decrease it.', True, (255, 255, 255), (0, 0, 0))
r3r = r3.get_rect()
r3r.centerx = window.get_rect().centerx
r3r.top =  400
r4= controlsfont.render('Press Space bar to Launch the Player.', True, (255, 255, 255), (0, 0, 0))
r4r = r4.get_rect()
r4r.centerx = window.get_rect().centerx
r4r.top =  450
r5= controlsfont.render('First to 3 Wins! Press P to Play or Q to quit', True, (255, 255, 255), (0, 0, 0))
r5r = r5.get_rect()
r5r.centerx = window.get_rect().centerx
r5r.top =  500
r6= basicfont.render('How To Play', True, (255, 255, 255), (0, 0, 0))
r6r = r6.get_rect()
r6r.centerx = window.get_rect().centerx
r6r.top =  200
g1= controlsfont.render('First to 3 Wins! Press I for instructions or Q to quit', True, (255, 255, 255), (0, 0, 0))
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
currentAngle = 3.14
moveTimer=0
somethingselected=False
currentlyselected=player(1, 'rm')
t=0
turn = 1
angle=3.14
running = True
state='menu'
gameball = ball(True)
count = 0

  
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
      window.blit(r5,r5r)
      window.blit(r6,r6r)
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
      count = 0
      collisionList = []
      for o in dis:
        for k in range (1 + count, len(dis)):
            if (getDistance(o.x + 25, o.y + 25, dis[k].x + 25, dis[k].y + 25) < 60):
                if ((o.hittime >= 80) and (dis[k].hittime >= 80)):
                    playerCollision(o, dis[k])
                    collisionList.append(dis[k])
        if (count != (len(dis) - 1)):
            count += 1
        if (getDistance(o.x + 25, o.y + 25, gameball.x + 10, gameball.y + 10) < 45):
          if (o.hittime >= 80):
              playerCollision(o, gameball)
        window.blit(o.piece,(o.x,o.y))
        o.move()
        for elements in dis:
            if (elements.hittime < 80):
                elements.hittime += 1

        if (o.isselected):
          pygame.draw.circle(window,(255,255,0),(int(o.x)+25,int(o.y)+25),26,2)
          draw_line(o, angle, 60)
      whoscored=gameball.move()
      if(whoscored!=0):
        if(whoscored==1):
          team2score+=1
          if(team2score==3):
            state='over'
        if(whoscored==2):
          team1score+=1
          if(team1score==3):
            state='over'
        dis=setupgame()
        currentAngle = 3.14
        moveTimer=0
        somethingselected=False
        currentlyselected=player(1, 'rm')
        t=0
        turn = 1
        gameball = ball(True)
        
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
            if event.key == pygame.K_i:#add instructions
                state='instructions'
            if event.key == pygame.K_w:#add instructions
                powerbar.add()
                pygame.display.update()
            if event.key == pygame.K_s:#add instructions
                powerbar.minus()
            if event.key == pygame.K_a:
                angle+=.1
            if event.key == pygame.K_d:
                angle-=.1
            if event.key == pygame.K_SPACE:
                currpow = powerbar.getpower()
                currpow*=3
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
      o1= controlsfont.render('Press A to Play Again or Q to Quit', True, (255, 255, 255), (0, 0, 0))
      o1r = o1.get_rect()
      o1r.centerx = window.get_rect().centerx
      o1r.top =  400
      window.blit(o1,o1r)
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:#add instructions
                running = False
            if event.key == pygame.K_a:
              dis=setupgame()
              team1score=0
              team2score=0
              state='game'

      pygame.display.update()


pygame.quit()
