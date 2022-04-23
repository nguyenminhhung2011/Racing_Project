import pygame, sys
import random
import time
from pygame.locals import*
import pygame
import pickle
import menuinrace

pygame.init()
WINDOWWIGTH = 1000	
WINDOWHEIGHT = 800
screen = pygame.display.set_mode((1000,600),RESIZABLE)
s = pygame.mixer.Sound("racing_car.wav")
d = pygame.mixer.Sound("tiressquealcorner.wav")
fpsclock = pygame.time.Clock()
#car in minigame
carminiimg = pygame.image.load('xe_chính-removebg-preview.png')
carMiNi_width = carminiimg.get_width()
carMiNi_height = carminiimg.get_height()
carMiNi_x = (1000 / 2) - carMiNi_width
carMiNi_y = 620 - carMiNi_height
carMiNi_speed = 3
X_Margin = 200
#Opstacles in minigame
Opstaclesimg = pygame.image.load('2-removebg-preview.png')
Opstacleswidth = Opstaclesimg.get_width()
Opstaclesheigth = Opstaclesimg.get_height()
lanewidth = 100
changespeed = 0.0005
distance = 400
Opstaclesspeed = 2
#backgroud in minigame
backgroudmimg = pygame.image.load('Layer 3 - Copy.jpg')
backgroudspeed = 2
backgroudwidth = backgroudmimg.get_width()
backgroudheight = backgroudmimg.get_height()

class Score():
	def __init__(self):
		self.score = 0
	def draw(self, screen):
		font = pygame.font.SysFont('Consolas', 30)
		scoreSurface = font.render('Score:' + str(int(self.score)), True, (255,0,0))
		screen.blit(scoreSurface, (10,10))
	def update(self):
		self.score += 0.02
		menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+int(self.score)*1000)

class Carmini():
	def __init__(self):
		self.img = carminiimg
		self.x = carMiNi_x
		self.y = carMiNi_y
		self.width = carMiNi_width
		self.height = carMiNi_height
		self.surface = pygame.Surface((self.width,self.height))
		self.surface.fill((255,255,255))
		self.speed = carMiNi_speed
		self.margin = X_Margin
	def draw(self, screen):
		screen.blit(self.img, (self.x, self.y))
	def update(self,moveUp,moveDown,moveLeft,moveRight):
		if moveUp == True:
			self.y -= self.speed
		if moveDown == True:
			self.y += self.speed
		if moveLeft == True:
			self.x -= self.speed
		if moveRight == True:
			self.x += self.speed
		if self.x < self.margin:
			self.x = self.margin
		if self.x > 800 - self.width:
			self.x = 800 - self.width
		if self.y < 0:
			self.y = 0
		if self.y > 650 - self.height:
			self.y = 650 - self.height

class Opstaclesmini():
	def __init__(self):
		self.img = Opstaclesimg
		self.height = Opstaclesheigth
		self.width = Opstacleswidth
		self.distance = distance
		self.speed = Opstaclesspeed
		self.changespeed = changespeed
		self.lane = lanewidth
		self.ls = []
		self.margin = X_Margin
		for i in range(4):
			y = -carMiNi_height - i*self.distance
			lane = random.randint(0,3)
			self.ls.append([lane,y])
	def draw(self,screen):
		for i in range(4):
			x = int( self.margin + self.ls[i][0] * self.lane + (self.lane - self.width)/2 )
			y = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		for i in range(4):
			self.ls[i][1] += self.speed
			self.speed += self.changespeed
		if self.ls[0][1] > 650:
			self.ls.pop(0) #xóa phần tử
			y = self.ls[2][1] - self.distance
			lane = random.randint(0, 3)
			self.ls.append([lane, y])

class BackGroudMiNiGame():
	def __init__(self):
		self.x = 100
		self.y = 0
		self.width = backgroudwidth
		self.height = backgroudheight
		self.speed = backgroudspeed
		self.img = backgroudmimg
	def draw(self,screen):
		screen.blit(self.img ,(int(self.x), int(self.y)))
		screen.blit(self.img, (int(self.x), int(self.y - self.height)))
	def update(self):
		self.y+=self.speed
		if self.y > self.height:
			self.y -= self.height
			
def rectcollision(rect1, rect2):
	if rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2] and rect1[1] <= rect2[1] + rect2[3] and rect2[1] <= rect1[1] + rect1[3]:
		return True
	return False

def gameover(carmini, opmini):
	carRect = [carmini.x, carmini.y, carmini.width, carmini.height]
	for i in range(4):
		x = int( opmini.margin + opmini.ls[i][0] * opmini.lane + (opmini.lane - opmini.width)/2 )
		y = int(opmini.ls[i][1])
		opRect = [x, y, opmini.width, opmini.height]
		if rectcollision(carRect, opRect) == True:
			return True
	return False
	

def gamestart():
	global click
	click=False
	bgmini.__init__()
	carmini.__init__()
	opmini.__init__()
	score.__init__()
	moveUp = False
	moveDown = False
	moveLeft = False
	moveRight = False
	while True:	
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_UP:
					moveUp = True
				if event.key == K_DOWN:
					moveDown = True
				if event.key == K_LEFT:
					moveLeft = True
				if event.key == K_RIGHT:
					moveRight = True
			if event.type == KEYUP:
				if event.key == K_UP:
					moveUp = False
				if event.key == K_DOWN:
					moveDown = False
				if event.key == K_LEFT:
					moveLeft = False
				if event.key == K_RIGHT:
					moveRight = False
		if gameover(carmini, opmini):
			menuinrace.racemenu(menuinrace.get_name())
	
		bgmini.draw(screen)
		bgmini.update()
		carmini.draw(screen)
		carmini.update(moveUp,moveDown,moveLeft,moveRight)
		opmini.draw(screen)
		opmini.update()
		score.draw(screen)
		score.update()
		pygame.display.update()
		fpsclock.tick(120)

	

bgmini = BackGroudMiNiGame()
carmini = Carmini()
opmini = Opstaclesmini()
score = Score()



		
