import pygame, sys 
from glob import glob
from pygame.locals import*
from pygame_functions import *
import random
import menuinrace


speedcar1 = random.randint(400,700)
speedcar2 = random.randint(400,700)
speedcar3 = random.randint(400,700)
speedcar4 = random.randint(400,700)
speedcar5 = random.randint(400,700)
speedcar6 = random.randint(400,700)

pygame.init()
fpsclock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800))
s = pygame.mixer.Sound("racing_car.wav")
t = pygame.mixer.Sound("tick.wav")
c = pygame.mixer.Sound("button.mp3")
w = pygame.mixer.Sound("win1.mp3")
backgroundmainimg= pygame.image.load('special-lap2.jpg')

def get_name(name):
	global username
	username = name

MARGIN = 100
#buadichchuyen
buadichchuyenimg = pygame.image.load('bua-nhanh.png')
buadichchuyenwidth = buadichchuyenimg.get_width()
buandichchuyenheight = buadichchuyenimg.get_height()
#buacham
buachamimg = pygame.image.load('bua-cham.png')
buachamwidth = buachamimg.get_width()
buachamheight = buachamimg.get_height()
#bua nhanh
buanhanhimg = pygame.image .load('fast-forward.png')
buanhanhwidth = buanhanhimg.get_width()
buanhanhheight = buanhanhimg.get_height()
#bua ve dich
buavedichimg = pygame.image.load('bua-tele.png')
buavedichwidth = buavedichimg.get_width()
buavedichheight = buavedichimg.get_height()
#bua bat dau lai
buabatdaulaiimg = pygame.image.load('bua-bat-dau-lai.png')
buabatdaulaiwidth = buabatdaulaiimg.get_width()
buabatdaulaiheight = buabatdaulaiimg.get_height()
backgroundmainimg1 = pygame.image.load('iron man/134404164_256418259236292_1122539562479276773_n.jpg')

class Save():
	def __init__(self):
		self.save = 0
	def update(self):
		self.save += (10 / 6)

class BuaVeDich():
	def __init__(self):
		self.img = buavedichimg
		self.width = buavedichwidth
		self.height = buavedichheight
		self.speed = 5
		self.distance = 1000000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   9000 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

class BuaCham():
	def __init__(self):
		self.img = buachamimg
		self.width = buachamwidth
		self.height = buachamheight
		self.speed = 7
		self.distance = 9000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   1000 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

class BuaNhanh():
	def __init__(self):
		self.img = buanhanhimg
		self.width = buanhanhwidth
		self.height = buanhanhheight
		self.speed = 5
		self.distance = 15000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   3000 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

class BuaDichChuyen():
	def __init__(self):
		self.img = buadichchuyenimg
		self.width = buadichchuyenwidth
		self.height = buandichchuyenheight
		self.speed = 5
		self.distance = 14000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   900 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])
	
class BuaBatDauLai():
	def __init__(self):
		self.img = buabatdaulaiimg
		self.width = buabatdaulaiwidth
		self.height = buabatdaulaiheight
		self.speed = 5
		self.distance = 200000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   2000 + i*self.distance
			lane = random.randint(0, 5)
			self.ls.append([lane,x])
	def drawinmaingame(self,screen):
		for i in range(6):
			y = int(MARGIN + self.ls[i][0]*100 + (100-self.width) / 2)
			x = int(self.ls[i][1])
			screen.blit(self.img,(x,y))
	def update(self):
		self.save += 10
		for i in range(6):
			if self.save > 0 and self.save < backgroundmainimg.get_width() - 3000:
				self.ls[i][1] -= self.speed
			else: self.ls[i][1] -= 0
		if self.ls[0][1] < 0:
			self.ls.pop(0)
			x = self.ls[2][1] - self.distance
			lane = random.randint(0,5)
			self.ls.append([lane,x])

class backgroundamin():
	def __init__(self):
		self.img = backgroundmainimg
		self.x = 0
		self.y = 0
		self.speed = 10
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.ans = 0	 
		self.save = 0
	def draw(self, screen):
		screen.blit(self.img,(int(self.x), int(self.y)))
		screen.blit(self.img, (int(self.x - self.width), int(self.y)))
	def update(self):
		self.save += self.speed 	
		self.x -= self.speed
		if self.save > self.width - 1000:
			self.speed = 0 

class HoangSpider:
	def __init__(self):
		self.x = 0
		self.y = 120
		self.list = [pygame.image.load(f).convert_alpha() for f in glob("spiderman/spider*.png")[1:]]
		self.counter = 0
		self.image = self.list[0]
		self.dir = "right"	
		self.save = 0
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.score = 0
		self.count = 10
	def draw(self, screen):
		self.counter += .1
		if self.counter >= len(self.list):
			self.counter = 0
		if self.dir == "right":
			self.image = self.list[int(self.counter)]
		screen.blit(self.image, (self.x, self.y))
	def update(self,hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width:
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen) == 5:
			self.x += 300
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 5:
			self.x += 1800 
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 5:
			self.x -= 5
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 5:
			self.x += 4
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 5:
			self.x -= self.x + self.save
		else:
			if self.save > speedcar1 and self.save < backgroundmainimg.get_width() - 1000:
				self.x += random.randint(-3,3)
			if self.save > backgroundmainimg.get_width() - 1000:
				self.x += 5
				if self.x > 1000 - self.width:
					self.x = 1000 - self.width
			if self.save < speedcar1:
				self.x += 2	
class GiaHulk:
	def __init__(self):
		self.x = 0
		self.y = 500
		self.list = [pygame.image.load(f).convert_alpha() for f in glob("hulk/hulk*.png")[1:]]
		self.counter = 0
		self.image = self.list[0]
		self.dir = "right"	
		self.save = 0
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.score = 0
		self.count = 10
	def draw(self, screen):
		self.counter += .1
		if self.counter >= len(self.list):
			self.counter = 0
		if self.dir == "right":
			self.image = self.list[int(self.counter)]
		screen.blit(self.image, (self.x, self.y))
	def update(self,hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width:
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen) == 2:
			self.x += 300
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 2:
			self.x += 1800
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 2:
			self.x -= 5
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 2:
			self.x += 4
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 2:
			self.x -= self.x + self.save
		else:
			if self.save > speedcar1 and self.save < backgroundmainimg.get_width() - 1000:
				self.x += random.randint(-3,3)
			if self.save > backgroundmainimg.get_width() - 1000:
				self.x += 5
				if self.x > 1000 - self.width:
					self.x = 1000 - self.width
			if self.save < speedcar1:
				self.x += 2		

class HaoCaptain:
	def __init__(self):
		self.x = 0
		self.y = 600
		self.list = [pygame.image.load(f).convert_alpha() for f in glob("captain/cap*.png")[1:]]
		self.counter = 0
		self.image = self.list[0]
		self.dir = "right"	
		self.save = 0
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.score = 0
		self.count = 10
	def draw(self, screen):
		self.counter += .1
		if self.counter >= len(self.list):
			self.counter = 0
		if self.dir == "right":
			self.image = self.list[int(self.counter)]
		screen.blit(self.image, (self.x, self.y))
	def update(self,hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width:
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen) == 3:
			self.x += 300
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 3:
			self.x += 1010
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 3:
			self.x -= 5
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 3:
			self.x += 4
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 3:
			self.x -= self.x + self.save
		else:
			if self.save > speedcar1 and self.save < backgroundmainimg.get_width() - 1000:
				self.x += random.randint(-3,3)
			if self.save > backgroundmainimg.get_width() - 1000:
				self.x += 5
				if self.x > 1000 - self.width:
					self.x = 1000 - self.width
			if self.save < speedcar1:
				self.x += 2	

class HieuBlack:
	def __init__(self):
		self.x = 0
		self.y = 200
		self.list = [pygame.image.load(f).convert_alpha() for f in glob("black/black*.png")[1:]]
		self.counter = 0
		self.image = self.list[0]
		self.dir = "right"
		self.save = 0
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.score = 0
		self.count = 10
	def draw(self,screen):
		self.counter += .1
		if self.counter >= len(self.list):
			self.counter = 0
		if self.dir == "right":
			self.image = self.list[int(self.counter)]
		screen.blit(self.image, (self.x, self.y))
	def update(self,hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width:
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen) == 4:
			self.x += 300
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 4:
			self.x += 1800
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 4:
			self.x -= 5
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 4:
			self.x += 4
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 4:
			self.x -= self.x + self.save
		else:
			if self.save > speedcar1 and self.save < backgroundmainimg.get_width() - 1000:
				self.x += random.randint(-3,3)
			if self.save > backgroundmainimg.get_width() - 1000:
				self.x += 5
				if self.x > 1000 - self.width:
					self.x = 1000 - self.width
			if self.save < speedcar1:
				self.x += 2	

class DuyIron:
	def __init__(self):
		self.x = 0
		self.y = 300
		self.list = [pygame.image.load(f).convert_alpha() for f in glob("iron man/iron*.png")[1:]]
		self.counter = 0
		self.image = self.list[0]
		self.dir = "right"
		self.save = 0 
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.score = 0
		self.count = 10
	def draw(self,screen):
		self.counter += .1
		if self.counter >= len(self.list):
			self.counter = 0
		if self.dir == "right":
			self.image = self.list[int(self.counter)]
		screen.blit(self.image, (self.x, self.y))
	def update(self,hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width:
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen) == 6:
			self.x += 400
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 6:
			self.x += 1800
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 6:
			self.x -= 5
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 6:
			self.x += 4
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 6:
			self.x -= self.x + self.save
		else:
			if self.save > speedcar1 and self.save < backgroundmainimg.get_width() - 1000:
				self.x += random.randint(-3,3)
			if self.save > backgroundmainimg.get_width() - 1000:
				self.x += 5
				if self.x > 1000 - self.width:
					self.x = 1000 - self.width
			if self.save < speedcar1:
				self.x += 2	

class HungThor:
	def __init__(self):
		self.x = 0
		self.y = 410
		self.list = [pygame.image.load(f).convert_alpha() for f in glob("thor/thor*.png")[1:]]
		self.counter = 0
		self.image = self.list[0]
		self.dir = "right"
		self.save = 0
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.score = 0
		self.count = 10
	def draw(self,screen):
		self.counter += .1
		if self.counter >= len(self.list):
			self.counter = 0
		if self.dir == "right":
			self.image = self.list[int(self.counter)]
		screen.blit(self.image, (self.x, self.y))
	def update(self,hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width:
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen) == 1:
			self.x += 300
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 1:
			self.x += 1800
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 1:
			self.x -= 5
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 1:
			self.x += 4
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 1:
			self.x -= self.x + self.save
		else:
			if self.save > speedcar1 and self.save < backgroundmainimg.get_width() - 1000:
				self.x += random.randint(-3,3)
			if self.save > backgroundmainimg.get_width() - 1000:
				self.x += 5
				if self.x > 1000 - self.width:
					self.x = 1000 - self.width
			if self.save < speedcar1:
				self.x += 2	

def Datcuoc1():
	global click
	global tien_thuong
	tien_thuong = 0
	hung = HungThor()
	gia = GiaHulk()
	hao = HaoCaptain()
	hieu = HieuBlack()
	hoang = HoangSpider()
	duy = DuyIron()
	while True:
		s.play()
		screen.fill(((0,0,0)))
		mx, my = pygame.mouse.get_pos()
		button_1 = screen.blit(pygame.image.load('5k.png'), (700,300))
		button_1img = pygame.image.load('5k.png')
		button_1width = button_1img.get_width()	
		button_2 = screen.blit(pygame.image.load('10k.png'), (700,400))
		button_2img = pygame.image.load('10k.png')
		button_2width = button_2img.get_width()	
		button_3 = screen.blit(pygame.image.load('25k.png'), (700, 500))
		button_3img = pygame.image.load('25k.png')
		button_3width = button_3img.get_width()	
		button_4 = screen.blit(pygame.image.load('50k.png'), (700,600))
		button_4img = pygame.image.load('50k.png')
		button_4width = button_4img.get_width()	
		button_5 = screen.blit(pygame.image.load('100k.png'), (700,700)) 
		button_5img = pygame.image.load('100k.png')
		button_5width = button_5img.get_width()	
		if button_1.collidepoint((mx, my)):
			if click:
				tien_thuong = 5000
				ChonXe(screen, hung, gia, hao, hieu, hoang, duy)
		if button_2.collidepoint((mx, my)):
			if click:
				tien_thuong = 10000	
				ChonXe(screen, hung, gia, hao, hieu, hoang, duy)
		if button_3.collidepoint((mx, my)):
			if click:
				tien_thuong = 25000
				ChonXe(screen, hung, gia, hao, hieu, hoang, duy)
		if button_4.collidepoint((mx, my)):
			if click:
				tien_thuong = 50000
				ChonXe(screen, hung, gia, hao, hieu, hoang, duy)
		if button_5.collidepoint((mx, my)):
			if click:
				tien_thuong = 100000
				ChonXe(screen, hung, gia, hao, hieu, hoang, duy)
		click = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('5k.png'), (700,300))
		screen.blit(pygame.image.load('10k.png'), (700,400))
		screen.blit(pygame.image.load('25k.png'), (700,500))
		screen.blit(pygame.image.load('50k.png'), (700,600))
		screen.blit(pygame.image.load('100k.png'), (700,700))
		pygame.display.update()
		fpsclock.tick(60)

click = False

hungimg = pygame.image.load('thor/thor (1).png')
giaimg = pygame.image.load('hulk/hulk (1).png')
hoangimg = pygame.image.load('spiderman/spider (1).png')
hieuimg = pygame.image.load('black/black (1).png')
haoimg = pygame.image.load('captain/cap (1).png')
duyimg = pygame.image.load('iron man/iron (1).png')

def ChonXe(screen, hung, gia, hao, hieu, hoang, duy):
	global click
	global xechon

	hung.__init__()
	gia.__init__()
	hao.__init__()
	hieu.__init__()
	hoang.__init__()
	duy.__init__()
	while True:
		s.play
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_1img = hungimg
		button_1width = button_1img.get_width()
		button_1 = screen.blit(hungimg, (int(1000 - button_1img.get_width()), 200))
		button_2img = giaimg
		button_2width = button_2img.get_width()
		button_2 = screen.blit(giaimg, (int(1000 - button_2img.get_width()), 300))
		button_3img = haoimg
		button_3width = button_3img.get_width()
		button_3 = screen.blit(haoimg, (int(1000 - button_3img.get_width()), 400))
		button_4img = hieuimg
		button_4width = button_4img.get_width()
		button_4 = screen.blit(hieuimg, (int(1000 - button_4img.get_width()), 500))
		button_5img = hoangimg
		button_5width = button_5img.get_width()
		button_5 = screen.blit(hoangimg, (int(1000 - button_5img.get_width()), 600))
		button_6img = duyimg
		button_6width = button_6img.get_width()
		button_6 = screen.blit(duyimg, (int(1000 - button_6img.get_width()), 700))
		if button_1.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 1
				special()
		if button_2.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 2
				special()
		if button_3.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 3
				special()
		if button_4.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 4
				special()
		if button_5.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 5
				special()
		if button_6.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 6
				special()
		click = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(hungimg, (int(1000 - hungimg.get_width()), 200))
		screen.blit(giaimg, (int(1000 - giaimg.get_width()), 300))
		screen.blit(haoimg, (int(1000 - haoimg.get_width()), 400))
		screen.blit(hieuimg, (int(1000 - hieuimg.get_width()), 500))
		screen.blit(hoangimg, (int(1000 - hoangimg.get_width()), 600))
		screen.blit(duyimg, (int(1000 - duyimg.get_width()), 700))
		pygame.display.update()
		fpsclock.tick(60) 	

def rectcollision(rect1, rect2):
	if rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2] and rect1[1] <= rect2[1] + rect2[3] and rect2[1] <= rect1[1] + rect1[3]:
		return True
	else :return False

def chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen):
	hungRect = [hung.x , hung.y, hung.width, hung.height]
	giaRect = [gia.x , gia.y, gia.width, gia.height]
	haoRect = [hao.x , hao.y, hao.width, hao.height]
	hieuRect = [hieu.x , hieu.y, hieu.width, hieu.height]
	hoangRect = [hoang.x , hoang.y, hoang.width, hoang.height]
	duyRect = [duy.x , duy.y, duy.width, duy.height]
	for i in range(6):
		y = int(MARGIN + buadichchuyen.ls[i][0]*100 + (100-buadichchuyen.width) / 2)
		x = int(buadichchuyen.ls[i][1])
		buadichchuyenRect = [x, y, buadichchuyen.width, buadichchuyen.height]
		if rectcollision(hungRect, buadichchuyenRect):
			return 1
		elif rectcollision(giaRect, buadichchuyenRect):
			return 2
		elif rectcollision(haoRect, buadichchuyenRect):
			return 3
		elif rectcollision(hieuRect, buadichchuyenRect):
			return 4
		elif rectcollision(hoangRect, buadichchuyenRect):
			return 5
		elif rectcollision(duyRect, buadichchuyenRect):
			return 6
		else :return False

def chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh):
	hungRect = [hung.x , hung.y, hung.width, hung.height]
	giaRect = [gia.x , gia.y, gia.width, gia.height]
	haoRect = [hao.x , hao.y, hao.width, hao.height]
	hieuRect = [hieu.x , hieu.y, hieu.width, hieu.height]
	hoangRect = [hoang.x , hoang.y, hoang.width, hoang.height]
	duyRect = [duy.x , duy.y, duy.width, duy.height]
	for i in range(6):
		y = int(MARGIN + buanhanh.ls[i][0]*100 + (100-buanhanh.width) / 2)
		x = int(buanhanh.ls[i][1])
		buanhanhRect = [x, y, buanhanh.width, buanhanh.height]
		if rectcollision(hungRect, buanhanhRect):
			return 1
		if rectcollision(giaRect, buanhanhRect):
			return 2
		if rectcollision(haoRect, buanhanhRect):
			return 3
		if rectcollision(hieuRect, buanhanhRect):
			return 4
		if rectcollision(hoangRect, buanhanhRect):
			return 5
		if rectcollision(duyRect, buanhanhRect):
			return 6
		else: return False

def chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham):
	hungRect = [hung.x , hung.y, hung.width, hung.height]
	giaRect = [gia.x , gia.y, gia.width, gia.height]
	haoRect = [hao.x , hao.y, hao.width, hao.height]
	hieuRect = [hieu.x , hieu.y, hieu.width, hieu.height]
	hoangRect = [hoang.x , hoang.y, hoang.width, hoang.height]
	duyRect = [duy.x , duy.y, duy.width, duy.height]
	for i in range(6):
		y = int(MARGIN + buacham.ls[i][0]*100 + (100-buacham.width) / 2)
		x = int(buacham.ls[i][1])
		buachamRect = [x, y, buacham.width, buacham.height]
		if rectcollision(hungRect, buachamRect):
			return 1
		if rectcollision(giaRect, buachamRect):
			return 2
		if rectcollision(haoRect, buachamRect):
			return 3
		if rectcollision(hieuRect, buachamRect):
			return 4
		if rectcollision(hoangRect, buachamRect):
			return 5
		if rectcollision(duyRect, buachamRect):
			return 6
		else: return False

def chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich):
	hungRect = [hung.x , hung.y, hung.width, hung.height]
	giaRect = [gia.x , gia.y, gia.width, gia.height]
	haoRect = [hao.x , hao.y, hao.width, hao.height]
	hieuRect = [hieu.x , hieu.y, hieu.width, hieu.height]
	hoangRect = [hoang.x , hoang.y, hoang.width, hoang.height]
	duyRect = [duy.x , duy.y, duy.width, duy.height]
	for i in range(6):
		y = int(MARGIN + buavedich.ls[i][0]*100 + (100-buavedich.width) / 2)
		x = int(buavedich.ls[i][1])
		buavedichRect = [x, y, buavedich.width, buavedich.height]
		if rectcollision(hungRect, buavedichRect):
			return 1
		elif rectcollision(giaRect, buavedichRect):
			return 2
		elif rectcollision(haoRect, buavedichRect):
			return 3
		elif rectcollision(hieuRect, buavedichRect):
			return 4
		elif rectcollision(hoangRect, buavedichRect):
			return 5
		elif rectcollision(duyRect, buavedichRect):
			return 6
		else: return False

def chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai):
	hungRect = [hung.x , hung.y, hung.width, hung.height]
	giaRect = [gia.x , gia.y, gia.width, gia.height]
	haoRect = [hao.x , hao.y, hao.width, hao.height]
	hieuRect = [hieu.x , hieu.y, hieu.width, hieu.height]
	hoangRect = [hoang.x , hoang.y, hoang.width, hoang.height]
	duyRect = [duy.x , duy.y, duy.width, duy.height]
	for i in range(6):
		y = int(MARGIN + buabatdaulai.ls[i][0]*100 + (100-buabatdaulai.width) / 2)
		x = int(buabatdaulai.ls[i][1])
		buabatdaulaiRect = [x, y, buabatdaulai.width, buabatdaulai.height]
		if rectcollision(hungRect, buabatdaulaiRect):
			return 1
		if rectcollision(giaRect, buabatdaulaiRect):
			return 2
		if rectcollision(haoRect, buabatdaulaiRect):
			return 3
		if rectcollision(hieuRect, buabatdaulaiRect):
			return 4
		if rectcollision(hoangRect, buabatdaulaiRect):
			return 5
		if rectcollision(duyRect, buabatdaulaiRect):
			return 6
		else: return False

click = False
def gamestart(bg, hoang, hieu, duy, hung, gia, hao, buadichchuyen, buavedich,buacham,buanhanh, buabatdaulai, save, screen):
	global angle
	global click
	from maingame import all_lap
	angle = 0
	bg.__init__()
	hoang.__init__()
	hieu.__init__()
	duy.__init__()
	hung.__init__()
	gia.__init__()
	hao.__init__()
	save.__init__()
	buadichchuyen.__init__()
	buavedich.__init__()
	buacham.__init__()
	buanhanh.__init__()
	buabatdaulai.__init__()
	while True:
		angle += 1
		screen.fill((0,0,0))
		mx ,my = pygame.mouse.get_pos()
		button_5 = screen.blit(pygame.image.load('back.png'), (10, 740))
		button_5img = pygame.image.load('back.png')
		if button_5.collidepoint((mx, my)):
			if click:
				w.stop()
				all_lap()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		bg.draw(screen)
		bg.update()

		hoang.draw(screen)
		hieu.draw(screen)
		duy.draw(screen)
		hung.draw(screen)
		hao.draw(screen)
		gia.draw(screen)

		hoang.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save)
		hieu.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save)
		duy.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save)
		hung.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save)
		hao.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save)
		gia.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buabatdaulai, buanhanh, save)

		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen)==1:
			hung.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 1:
			hung.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 1:
			hung.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 1:
			hung.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 1:
			hung.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen)==2:
			gia.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 2:
			gia.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 2:
			gia.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 2:
			gia.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 2:
			gia.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen)==3:
			hao.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 3:
			hao.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 3:
			hao.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 3:
			hao.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 3:
			hao.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen)==4:
			hieu.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 4:
			hieu.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 4:
			hieu.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 4:
			hieu.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 4:
			hieu.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen)==5:
			hoang.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 5:
			hoang.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 5:
			hoang.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 5:
			hoang.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 5:
			hoang.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
			
		if chamBuadichchuyen(hung, gia, hao, hieu, hoang, duy, buadichchuyen)==6:
			duy.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaVeDich(hung, gia, hao, hieu, hoang, duy, buavedich) == 6:
			duy.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaLamCham(hung, gia, hao, hieu, hoang, duy, buacham) == 6:
			duy.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaNhanh(hung, gia, hao, hieu, hoang, duy, buanhanh) == 6:
			duy.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		elif chamBuaBatDauLai(hung, gia, hao, hieu, hoang, duy, buabatdaulai) == 6:
			duy.update(hung, gia, hao, hieu, hoang, duy, buadichchuyen, buavedich, buacham, buanhanh, buabatdaulai, save)
		
		buacham.drawinmaingame(screen)
		buacham.update()

		buadichchuyen.drawinmaingame(screen)
		buadichchuyen.update()

		buavedich.drawinmaingame(screen)
		buavedich.update()

		buabatdaulai.drawinmaingame(screen)
		buabatdaulai.update()

		if hung.count + gia.count + hao.count + hieu.count + hoang.count + duy.count == 0	:
			screen.blit(backgroundmainimg1, (0,0))
			screen.blit(button_5img, (10, 740))
			s.stop()
			w.play()
			if hung.score == min(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score):
				screen.blit(pygame.transform.rotate(hungimg, angle), (int(1000 - hungimg.get_width()) / 2, 330))
				if xechon == 1:
					menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong * 2)
			elif hung.score == max(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score) and xechon == 1:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien() - tien_thuong)
			else:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong)
			if gia.score == min(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score):
				screen.blit(pygame.transform.rotate(giaimg, angle), (int(1000 - giaimg.get_width()) 	/ 2, 330))
				if xechon == 2:
					menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong * 2)
			elif gia.score == max(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score) and xechon == 2:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien() - tien_thuong)
			else:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong)
			if hao.score == min(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score):
				screen.blit(pygame.transform.rotate(haoimg, angle), (int(1000 - haoimg.get_width()) / 2, 330))
				if xechon == 3:
					menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong * 2)
			elif hao.score == max(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score) and xechon == 3:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien() - tien_thuong)
			else:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong)
			if hieu.score == min(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score):
				screen.blit(pygame.transform.rotate(hieuimg, angle), (int(1000 - hieuimg.get_width()) / 2, 330))
				if xechon == 4:
					menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong * 2)
			elif hieu.score == max(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score) and xechon == 4:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien() - tien_thuong)
			else:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong)
			if hoang.score == min(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score):
				screen.blit(pygame.transform.rotate(hoangimg, angle), (int(1000 - hoangimg.get_width()) / 2, 330))
				if xechon == 5:
					menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong * 2)
			elif hoang.score == max(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score) and xechon == 5:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien() - tien_thuong)
			else:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong)
			if duy.score == min(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score):
				screen.blit(pygame.transform.rotate(duyimg, angle), (int(1000 - duyimg.get_width()) / 2, 330))
				if xechon == 6:
					menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong * 2)
			elif duy.score == max(hung.score, gia.score, hao.score, hieu.score, hoang.score, duy.score) and xechon == 6:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien() - tien_thuong)
			else:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong)

		pygame.display.update()
		fpsclock.tick(120)

def special():
	bg = backgroundamin()
	hoang = HoangSpider()
	hieu = HieuBlack()
	duy = DuyIron()
	hung = HungThor()
	hao = HaoCaptain()
	gia = GiaHulk()
	buadichchuyen = BuaDichChuyen()
	buavedich = BuaVeDich()
	buacham = BuaCham()
	buanhanh = BuaNhanh()
	buabatdaulai = BuaBatDauLai()
	save = Save()
	while True:
		gamestart(bg, hoang, hieu, duy, hung, gia, hao, buadichchuyen, buavedich,buacham,buanhanh, buabatdaulai, save, screen)