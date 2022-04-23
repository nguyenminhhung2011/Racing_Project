import pygame, sys
from pygame.locals import*
import minigame 
from random import randint 
import maingame 
import time



storeimg = pygame.image.load('store.png')
storewidth = storeimg.get_width()
storeheight = storeimg.get_height()
	
pygame.init()
m = pygame.mixer.Sound("move.wav")
s = pygame.mixer.Sound("tokyo_drift.mp3")
fpsclock = pygame.time.Clock()
 
WINDOWWIGTH = 1000	
WINDOWHEIGHT = 800
screen = pygame.display.set_mode((WINDOWWIGTH,WINDOWHEIGHT))
font = pygame.font.SysFont('Colonna MT', 100)

def draw_text(text, font , color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y) 
	surface.blit(textobj, textrect)

def draw_word(word):
	font_name = pygame.font.SysFont('Consolas', 40)
	nameSurface = font_name.render(str(word), True, (0,0,0))
	screen.blit(nameSurface, (500, 15))

click = False

def race_menu(name,tien):
	
	global click
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_1img = pygame.image.load('race-button.png')
		button_1width = button_1img.get_width()
		button_1 = screen.blit(pygame.image.load('race-button.png'), (int(1000 - button_1width) / 2,350))
		button_2img = pygame.image.load('minigame-button.png')
		button_2width = button_2img.get_width()
		button_2 = screen.blit(pygame.image.load('minigame-button.png'), (int(1000 - button_2width) / 2,450))
		button_3img = pygame.image.load('shop-button.png')
		button_3width = button_3img.get_width()	
		button_3 = screen.blit(pygame.image.load('shop-button.png'), (int(1000 - button_3width) / 2,550))
		button_4img = pygame.image.load('menu.png')
		button_4width = button_4img.get_width()	
		button_4 = screen.blit(pygame.image.load('menu.png'), (int(1000 - button_4width) / 2,150))

		if button_1.collidepoint((mx, my)):
			if click:
				s.stop()
				m.play()
				time.sleep(1)
				maingame.all_lap()
		if button_2.collidepoint((mx, my)):
			if click:
				s.stop()
				click=False
				minigame.gamestart()	
		if button_3.collidepoint((mx, my)):
			if click:
				s.stop()

				m.play()
				menuinstore(name,tien)
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
	
		
		screen.blit(pygame.image.load('race-button.png'), (int(1000 - button_1width) / 2,350))
		screen.blit(pygame.image.load('minigame-button.png'), (int(1000 - button_2width) / 2,450))
		screen.blit(pygame.image.load('shop-button.png'), (int(1000 - button_3width) / 2,550))
		screen.blit(pygame.image.load('menu.png'), (int(1000 - button_4width) / 2,150))

		screen.blit(pygame.image.load('Name.png'), (0,0))
		screen.blit(pygame.image.load('cash-khung.png'), (0,70))

		font_money = pygame.font.SysFont('Consolas', 20)
		moneySurface = font_money.render(str(tien), True, (30,144,255))
		screen.blit(moneySurface, (90, 134))

		font_name = pygame.font.SysFont('Consolas', 20)
		nameSurface = font_name.render(str(name), True, (211,211,211))
		screen.blit(nameSurface, (90, 60))

		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		
		pygame.display.update()
		fpsclock.tick(60)


def menuinstore(name,tien):
	global click
	global check_buy 
	check_buy=False
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_1img = pygame.image.load('charm_button.png') 
		button_1width = button_1img.get_width()
		button_1 = screen.blit(pygame.image.load('charm_button.png'), (int(1000 - button_1width) / 2,360))
		button_2img = pygame.image.load('car_button.png') 
		button_2width = button_1img.get_width()
		button_2 = screen.blit(pygame.image.load('car_button.png'), (int(1000 - button_2width) / 2,260))
		button_3img = pygame.image.load('back.png') 
		button_3width = button_1img.get_width()
		button_3 = screen.blit(pygame.image.load('back.png'), (10,740))           
	
		if button_3.collidepoint((mx, my)):
			if click:
				s.stop()
				m.play()
				race_menu(name,tien)
		if button_1.collidepoint((mx, my)):
			if click:
				s.stop()
				m.play()
				Bua(name,tien)
		if button_2.collidepoint((mx, my)):
			if click:
				s.stop()
				m.play()
				Car(name,tien)
				
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		draw_text('STORE', font, (0,0,0), screen, 300,200)
		screen.blit(pygame.image.load('charm_button.png'), (int(1000 - button_1width) / 2,360))
		screen.blit(pygame.image.load('car_button.png'), (int(1000 - button_2width) / 2,260))
		screen.blit(pygame.image.load('back.png'), (10,740))

		screen.blit(pygame.image.load('Name.png'), (0,0))
		screen.blit(pygame.image.load('cash-khung.png'), (0,70))

		font_money = pygame.font.SysFont('Consolas', 20)
		moneySurface = font_money.render(str(tien), True, (30,144,255))
		screen.blit(moneySurface, (90, 134))

		font_name = pygame.font.SysFont('Consolas', 20)
		nameSurface = font_name.render(str(name), True, (211,211,211))
		screen.blit(nameSurface, (90, 60))

		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		
		pygame.display.update()
		fpsclock.tick(60)

def Car(name,tien):
	
	global click
	global skin
	global chon
	while True:	
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_1 = pygame.Rect(10,745,200,50)
		
		button_2img = pygame.image.load('1-removebg-preview (2).png')
		button_2width = button_2img.get_width()
		button_2 = screen.blit(pygame.image.load('1-removebg-preview (2).png'), (230,250))

		button_3img = pygame.image.load('2-removebg-preview (1).png')
		button_3width = button_3img.get_width()
		button_3 = screen.blit(pygame.image.load('2-removebg-preview (1).png'), (700,250))

		button_4img = pygame.image.load('4-removebg-preview (2).png')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('4-removebg-preview (2).png'), (230,360))

		button_5img = pygame.image.load('3-removebg-preview (2).png')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('3-removebg-preview (2).png'), (700,360))

		button_6img = pygame.image.load('5-removebg-preview (3).png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('5-removebg-preview (3).png'), (230,470))

		button_7img = pygame.image.load('xe2.png')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('xe2.png'), (700,470))

		button_8img = pygame.image.load('xe3.png')
		button_8width = button_8img.get_width()
		button_8 = screen.blit(pygame.image.load('xe3.png'), (230,580))

		button_9img = pygame.image.load('xe4.png')
		button_9width = button_9img.get_width()
		button_9 = screen.blit(pygame.image.load('xe4.png'), (700,580))

		button_10img = pygame.image.load('xe5.png')
		button_10width = button_10img.get_width()
		button_10 = screen.blit(pygame.image.load('xe5.png'), (230,690))

		button_11img = pygame.image.load('xe6.png')
		button_11width = button_11img.get_width()
		button_11 = screen.blit(pygame.image.load('xe6.png'), (700,690))


		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(storeimg,((int(1000 - storewidth) / 2), (int(800 - storeheight) / 2)))
		screen.blit(pygame.image.load('1-removebg-preview (2).png'), (230,250))
		screen.blit(pygame.image.load('2-removebg-preview (1).png'), (700,250))
		screen.blit(pygame.image.load('4-removebg-preview (2).png'), (230,360))
		screen.blit(pygame.image.load('3-removebg-preview (2).png'), (700,360))
		screen.blit(pygame.image.load('5-removebg-preview (3).png'), (230,470))
		screen.blit(pygame.image.load('xe2.png'), (700,470))
		screen.blit(pygame.image.load('xe3.png'), (230,580))
		screen.blit(pygame.image.load('xe4.png'), (700,580))
		screen.blit(pygame.image.load('xe5.png'), (230,690))
		screen.blit(pygame.image.load('xe6.png'), (700,690))
		pygame.draw.rect(screen,(0,0,0), button_1)

		screen.blit(pygame.image.load('Name.png'), (0,0))
		screen.blit(pygame.image.load('cash-khung.png'), (0,70))

		font_money = pygame.font.SysFont('Consolas', 20)
		moneySurface = font_money.render(str(tien), True, (30,144,255))
		screen.blit(moneySurface, (90, 134))

		font_name = pygame.font.SysFont('Consolas', 20)
		nameSurface = font_name.render(str(name), True, (211,211,211))
		screen.blit(nameSurface, (90, 60))

		if button_1.collidepoint((mx, my)):
			if click:
				s.stop()
				m.play()
				menuinstore(name,tien)
				
		if button_2.collidepoint((mx, my)):
			if click:
				s.stop()
				m.play()
				if tien>=5000:
					tien-=5000
					chon = 1
					skin = button_2img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()
				
		if button_3.collidepoint((mx, my)):
			if click:
				m.play()
				s.stop()
				if tien>=5000:
					tien-=5000
					chon = 1
					skin = button_3img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()


		if button_4.collidepoint((mx, my)):
			if click:
				m.play()
				s.stop()
				if tien>=5000:
					tien-=5000
					chon = 1
					skin = button_4img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()

		if button_5.collidepoint((mx, my)):
			if click:
				m.play()
				s.stop()
				if tien>=5000:
					tien-=5000
					chon = 1
					skin = button_5img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()
			
		if button_6.collidepoint((mx, my)):
			if click:
				m.play()
				s.stop()
				if tien>=5000:
					tien-=5000
					chon = 1
					skin = button_6img
					draw_word("Da mua")
				else :
					draw_word("Khong du tien")
				pygame.display.update()
		
		if button_7.collidepoint((mx, my)):
			if click:
				m.play()
				s.stop()
				if tien>=5000:
					tien-=5000
					chon = 1
					skin = button_7img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()

		if button_8.collidepoint((mx, my)):
			if click:
				m.play()
				s.stop()
				if tien>=5000:
					tien-=5000
					chon = 1
					skin = button_8img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()

		if button_9.collidepoint((mx, my)):
			if click:
				m.play()
				s.stop()
				if tien>=5000:
					tien-=5000
					skin = button_9img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()

		if button_10.collidepoint((mx, my)):
			if click:
				m.play()
				s.stop()
				if tien>=5000:
					tien-=5000
					chon = 1
					skin = button_10img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()

		if button_11.collidepoint((mx, my)):
			if click:
				m.play()
				s.stop()
				if tien>=5000:
					tien-=5000
					chon = 1
					skin = button_11img
					draw_word("Da mua")
				else :
					chon = 0
					draw_word("Khong du tien")
				pygame.display.update()

		
		save_data(name,tien)
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		pygame.display.update()
		fpsclock.tick(60)
 


def random_bua(name,tien):
	global click
	
	k=0
	while True:		
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))

		bat_dau_lai_img = pygame.image.load('bat-dau-lai1.png')
		bat_dau_lai_width = bat_dau_lai_img.get_width()

		bua_cham_img = pygame.image.load('bua-cham1.png')
		bua_cham_width = bua_cham_img.get_width()

		bua_dung_img = pygame.image.load('bua-dung-yen1.png')
		bua_dung_width = bua_dung_img.get_width()

		bua_nhanh_img = pygame.image.load('bua-nhanh1.png')
		bua_nhanh_width = bua_nhanh_img.get_width()

		bua_quay_lui_img = pygame.image.load('bua-quay-lui1.png')
		bua_quay_lui_width = bua_quay_lui_img.get_width()

		bua_tele_img = pygame.image.load('bua-ve-dich1.png')
		bua_tele_width = bua_tele_img.get_width()

		bua_ve_dich_img = pygame.image.load('bua-nhanh1.png')
		bua_ve_dich_width = bua_ve_dich_img.get_width()
		
		button_6img = pygame.image.load('back.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('back.png'), (10, 740))
		

	
		if k<=0.8:
			
			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bat_dau_lai_img, (int(1000 - bat_dau_lai_width) / 2,300))
			pygame.display.update()
	
			time.sleep(k)

			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bua_cham_img, (int(1000 - bua_cham_width) / 2,300))
			pygame.display.update()
			
			time.sleep(k)

			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bua_dung_img, (int(1000 - bua_dung_width) / 2,300))
			pygame.display.update()
		
			time.sleep(k)

			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bua_nhanh_img, (int(1000 - bua_nhanh_width) / 2,300))
			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			pygame.display.update()
		
			time.sleep(k)
			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bua_quay_lui_img, (int(1000 - bua_quay_lui_width) / 2,300))
			pygame.display.update()
		
			time.sleep(k)

			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bua_tele_img, (int(1000 - bua_tele_width) / 2,300))
			pygame.display.update()
	
			time.sleep(k)

			screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
			screen.blit(bua_ve_dich_img, (int(1000 - bua_ve_dich_width) / 2,300))
			pygame.display.update()

			time.sleep(k)

		k=k+0.2

		random=randint(1,7)
		if k==1.2:
			

			if random == 1 :
				s.stop()

				screen.blit(bat_dau_lai_img, (int(1000 - bat_dau_lai_width) / 2,300))
				pygame.display.update()
		
			elif random == 2: 
				s.stop()
			
				screen.blit(bua_cham_img, (int(1000 - bua_cham_width) / 2,300))
				pygame.display.update()
				
			elif random == 3:
				s.stop()
			
				screen.blit(bua_dung_img, (int(1000 - bua_dung_width) / 2,300))
				pygame.display.update()
			
			elif random == 4:
				s.stop()
				
				screen.blit(bua_nhanh_img, (int(1000 - bua_nhanh_width) / 2,300))
				pygame.display.update()
			
			elif random == 5:
				s.stop()
				
				screen.blit(bua_quay_lui_img, (int(1000 - bua_quay_lui_width) / 2,300))
				pygame.display.update()
		
			elif random == 6:
				s.stop()
			
				screen.blit(bua_tele_img, (int(1000 - bua_tele_width) / 2,300))
				pygame.display.update()
			
			elif random == 7:
				s.stop()
				
				screen.blit(bua_ve_dich_img, (int(1000 - bua_ve_dich_width) / 2,300))
				pygame.display.update

			screen.blit(pygame.image.load('back.png'), (10, 740))
			pygame.display.update()

			screen.blit(pygame.image.load('Name.png'), (0,0))
			screen.blit(pygame.image.load('cash-khung.png'), (0,70))

			font_money = pygame.font.SysFont('Consolas', 20)
			moneySurface = font_money.render(str(tien), True, (30,144,255))
			screen.blit(moneySurface, (90, 134))

			font_name = pygame.font.SysFont('Consolas', 20)
			nameSurface = font_name.render(str(name), True, (211,211,211))
			screen.blit(nameSurface, (90, 60))

				
		if button_6.collidepoint((mx, my)):
			if click:
				menuinstore(name,tien)
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True 
		
		fpsclock.tick(60)
			
def Bua(name,tien):	
	global click
	while True:

		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()

		button_1img = pygame.image.load('hop qua bi an.png')
		button_1 = screen.blit(pygame.image.load('hop qua bi an.png'), (200, 300))

		button_6img = pygame.image.load('back.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('back.png'), (10, 740))
		
		if button_6.collidepoint((mx, my)):
			if click:
				s.stop()
				m.play()
				menuinstore(name,tien)
		if button_1.collidepoint((mx, my)):
			if click:
				m.play()
				tien=-5000
				save_data(name,tien)
				random_bua(name,tien)
		
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		draw_text('BUA', font ,(0,255,0), screen ,300 , 200)
		screen.blit(pygame.image.load('hop qua bi an.png'), (300,300))
		screen.blit(pygame.image.load('back.png'), (10, 740))

		screen.blit(pygame.image.load('Name.png'), (0,0))
		screen.blit(pygame.image.load('cash-khung.png'), (0,100))

		font_money = pygame.font.SysFont('Consolas', 20)
		moneySurface = font_money.render(str(tien), True, (30,144,255))
		screen.blit(moneySurface, (25, 170))

		font_name = pygame.font.SysFont('Consolas', 20)
		nameSurface = font_name.render(str(name), True, (211,211,211))
		screen.blit(nameSurface, (70, 60))



		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True 
		
		pygame.display.update()
		fpsclock.tick(60)
	
computer = randint(0,5)


def racemenu(username):
	global mk
	global tien
	global name
	global skin
	global chon 
	chon = 0
	name=username
	file = open(username+".txt","r")
	info=file.readlines(0)
	file.close()
	mk=info[1].strip()
	tien=int(info[2].strip())
	#skin=int(info[2].strip())
	while True:
		race_menu(name,tien)
		
def save_data(name,tien):
	file = open(name+".txt","w")
	file.write(name+"\n")
	file.write(mk+"\n")
	file.write(str(tien)+"\n")
	file.close()

def get_tien():
	return tien

def get_name():
	return name

def get_skin():
	return skin

def get_chon():
	return chon