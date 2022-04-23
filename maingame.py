import pygame, sys
import random
from pygame.locals import*
import pygame
import pickle 
import time
from special_race import*
import menuinrace

pygame.init()
s = pygame.mixer.Sound("racing_car.wav")
t = pygame.mixer.Sound("tick.wav")
c = pygame.mixer.Sound("button.mp3")
w = pygame.mixer.Sound("win1.mp3")
fpsclock = pygame.time.Clock()

screen = pygame.display.set_mode((1000,800))

def get_name(name):
	global username
	username = name
#RACE 
def draw_text(text, font , color, surface, x, y):                                        
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y) 
	surface.blit(textobj, textrect)	
click = False
def all_lap():
	from menuinrace import racemenu
	global click
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_1img = pygame.image.load('lap1-city (1).png')
		button_1width = button_1img.get_width()
		button_1 = screen.blit(pygame.image.load('lap1-city (1).png'), (200, 300))
		button_2img = pygame.image.load('lap-2-forest.jpg')
		button_2width = button_2img.get_width()
		button_2 = screen.blit(pygame.image.load('lap-2-forest.jpg'), (320,300))
		button_3img = pygame.image.load('lap3-thao-nguyen.jpg')
		button_3width = button_3img.get_width()
		button_3 = screen.blit(pygame.image.load('lap3-thao-nguyen.jpg '), (440, 300))
		button_4img = pygame.image.load('lap4-sahara.jpg')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('lap4-sahara.jpg'), (560, 300))
		button_5img = pygame.image.load('lap5-snow.jpg')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('lap5-snow.jpg'), (680, 300))
		button_6img = pygame.image.load('back.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('back.png'), (10, 740))
		button_7img = pygame.image.load('avenger-lap.jpg')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('avenger-lap.jpg'), (int(1000 - button_7img.get_width()) / 2, 580))
		if button_1.collidepoint((mx, my)):
			if click:
				s.stop()
				c.play()
				time.sleep(1)
				lap1()
		if button_2.collidepoint((mx, my)):
			if click:
				s.stop()
				c.play()
				time.sleep(1)
				lap2()
		if button_3.collidepoint((mx, my)):
			if click:
				s.stop()
				c.play()
				time.sleep(1)
				lap3()
		if button_4.collidepoint((mx, my)):
			if click:
				s.stop()
				c.play()
				time.sleep(1)
				lap4()
		if button_5.collidepoint((mx, my)):
			if click:
				s.stop()
				c.play()
				time.sleep(1)
				lap5()
		if button_6.collidepoint((mx, my)):
			if click:
				s.stop()
				c.play()
				time.sleep(1)
				racemenu(username)
		if button_7.collidepoint((mx, my)):
			if click:
				c.play()
				Datcuoc1()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('lap1-city (1).png'), (200, 300))	
		screen.blit(pygame.image.load('lap-2-forest.jpg'), (320,300))	
		screen.blit(pygame.image.load('lap3-thao-nguyen.jpg'), (440, 300))	
		screen.blit(pygame.image.load('lap4-sahara.jpg'), (560, 300))
		screen.blit(pygame.image.load('lap5-snow.jpg'), (680, 300))
		screen.blit(pygame.image.load('back.png'), (10, 740))
		screen.blit(pygame.image.load('avenger-lap.jpg'), (int(1000 - button_7img.get_width()) / 2, 580))

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

def lap1():
	global click
	global backgroundmainimg
	global carmainimg
	global carconlaiimg1
	global carconlaiimg2
	global carconlaiimg3
	global carconlaiimg4
	global carconlaiimg5
	global carconlaiimg1_copy
	global carconlaiimg2_copy
	global carconlaiimg3_copy
	global carconlaiimg4_copy
	global carconlaiimg5_copy
	global carmainimg_copy
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_4img = pygame.image.load('short-lap.png')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		button_5img = pygame.image.load('medium-lap.png')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		button_6img = pygame.image.load('long-lap.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		button_7img = pygame.image.load('back.png')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('back.png'), (10, 740))
		if button_4.collidepoint((mx, my)):
			if click:
				c.play()
				backgroundmainimg = pygame.image.load('15000.jpg')
				carmainimg = pygame.image.load('1-removebg-preview.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-qzb785D9o5us-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-sRfXJI9lv6i-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-W103PqtRbF-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-pgZ5wMLMHKnhrc-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-znj9cS7OM9kr1f-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)				
				Datcuoc()
				time.sleep(1)
		if button_5.collidepoint((mx, my)):
			if click:
				c.play()
				backgroundmainimg =  pygame.image.load('lap1(medium).jpg')
				carmainimg = pygame.image.load('1-removebg-preview.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-qzb785D9o5us-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-sRfXJI9lv6i-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-W103PqtRbF-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-pgZ5wMLMHKnhrc-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-znj9cS7OM9kr1f-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_6.collidepoint((mx, my)):
			if click:
				c.play()
				backgroundmainimg = pygame.image.load('lap1(long).jpg')
				carmainimg = pygame.image.load('1-removebg-preview.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-qzb785D9o5us-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-sRfXJI9lv6i-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-W103PqtRbF-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-pgZ5wMLMHKnhrc-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-znj9cS7OM9kr1f-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_7.collidepoint((mx, my)):
			if click:
				c.play()
				all_lap()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		screen.blit(pygame.image.load('back.png'), (10, 740))
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

def lap2():
	global click
	global backgroundmainimg
	global carmainimg
	global carconlaiimg1
	global carconlaiimg2
	global carconlaiimg3
	global carconlaiimg4
	global carconlaiimg5
	global carconlaiimg1_copy
	global carconlaiimg2_copy
	global carconlaiimg3_copy
	global carconlaiimg4_copy
	global carconlaiimg5_copy
	global carmainimg_copy
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_4img = pygame.image.load('short-lap.png')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		button_5img = pygame.image.load('medium-lap.png')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		button_6img = pygame.image.load('long-lap.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		button_7img = pygame.image.load('back.png')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('back.png'), (10, 740))
		if button_4.collidepoint((mx, my)):
			if click:
				c.play()
				backgroundmainimg = pygame.image.load('lap2(short).jpg')
				carmainimg = pygame.image.load('2.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('3.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('4.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('5.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('6.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('133649892_429212824870899_5158470857570509952_n.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_5.collidepoint((mx, my)):
			if click:
				c.play()
				backgroundmainimg = pygame.image.load('lap2(med).jpg')
				carmainimg = pygame.image.load('2.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('3.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('4.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('5.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('6.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('133649892_429212824870899_5158470857570509952_n.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_6.collidepoint((mx, my)):
			if click:
				backgroundmainimg = pygame.image.load('lap2(long).jpg')
				carmainimg = pygame.image.load('2.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('3.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('4.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('5.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('6.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('133649892_429212824870899_5158470857570509952_n.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_7.collidepoint((mx, my)):
			if click:
				c.play()
				all_lap()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		screen.blit(pygame.image.load('back.png'), (10, 740))
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

def lap3():
	global click
	global backgroundmainimg
	global carmainimg
	global carconlaiimg1
	global carconlaiimg2
	global carconlaiimg3
	global carconlaiimg4
	global carconlaiimg5
	global carconlaiimg1_copy
	global carconlaiimg2_copy
	global carconlaiimg3_copy
	global carconlaiimg4_copy
	global carconlaiimg5_copy
	global carmainimg_copy
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_4img = pygame.image.load('short-lap.png')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		button_5img = pygame.image.load('medium-lap.png')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		button_6img = pygame.image.load('long-lap.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		button_7img = pygame.image.load('back.png')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('back.png'), (10, 740))
		if button_4.collidepoint((mx, my)):
			if click:
				c.play()
				backgroundmainimg = pygame.image.load('lap3(short).jpg')
				carmainimg = pygame.image.load('imgonline-com-ua-ReplaceColor-3CPwUBXACNCJDmr-removebg-preview.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-10Vjk6ycJW-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-Kx1mHo0TNxkgkpa-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-uyU6jChFqRf-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-VBPaZbh0URBl-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-VOeBXJQug5mUWj8c-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_5.collidepoint((mx, my)):
			if click:
				c.play()
				backgroundmainimg = pygame.image.load('lap3(medium).jpg')
				carmainimg = pygame.image.load('imgonline-com-ua-ReplaceColor-3CPwUBXACNCJDmr-removebg-preview.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-10Vjk6ycJW-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-Kx1mHo0TNxkgkpa-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-uyU6jChFqRf-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-VBPaZbh0URBl-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-VOeBXJQug5mUWj8c-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_6.collidepoint((mx, my)):
			if click:
				backgroundmainimg = pygame.image.load('lap3(long).jpg')
				carmainimg = pygame.image.load('imgonline-com-ua-ReplaceColor-3CPwUBXACNCJDmr-removebg-preview.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-10Vjk6ycJW-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-Kx1mHo0TNxkgkpa-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-uyU6jChFqRf-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-VBPaZbh0URBl-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-VOeBXJQug5mUWj8c-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_7.collidepoint((mx, my)):
			if click:
				c.play()
				all_lap()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		screen.blit(pygame.image.load('back.png'), (10, 740))
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

def lap4():
	global click
	global backgroundmainimg
	global carmainimg
	global carconlaiimg1
	global carconlaiimg2
	global carconlaiimg3
	global carconlaiimg4
	global carconlaiimg5
	global carconlaiimg1_copy
	global carconlaiimg2_copy
	global carconlaiimg3_copy
	global carconlaiimg4_copy
	global carconlaiimg5_copy
	global carmainimg_copy
	while True:
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_4img = pygame.image.load('short-lap.png')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		button_5img = pygame.image.load('medium-lap.png')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		button_6img = pygame.image.load('long-lap.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		button_7img = pygame.image.load('back.png')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('back.png'), (10, 740))
		if button_4.collidepoint((mx, my)):
			if click:
				c.play()
				backgroundmainimg = pygame.image.load('lap4(short).jpg')
				carmainimg = pygame.image.load('132978159_812940865947444_815904502322492709_n.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-7I9O3ckmIbXb0-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-Hkmy1yQwYa-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-rhv0pm7mTE1eA-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-xHVYigNvCgefD-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-yHH1YhmDJiwN8T-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_5.collidepoint((mx, my)):
			if click:
				c.play()
				backgroundmainimg = pygame.image.load('lap4(medium).jpg')
				carmainimg = pygame.image.load('132978159_812940865947444_815904502322492709_n.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-7I9O3ckmIbXb0-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-Hkmy1yQwYa-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-rhv0pm7mTE1eA-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-xHVYigNvCgefD-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-yHH1YhmDJiwN8T-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_6.collidepoint((mx, my)):
			if click:
				c.play()
				backgroundmainimg = pygame.image.load('lap4(long).jpg')
				carmainimg = pygame.image.load('132978159_812940865947444_815904502322492709_n.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('imgonline-com-ua-ReplaceColor-7I9O3ckmIbXb0-removebg-preview.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('imgonline-com-ua-ReplaceColor-Hkmy1yQwYa-removebg-preview.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('imgonline-com-ua-ReplaceColor-rhv0pm7mTE1eA-removebg-preview.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('imgonline-com-ua-ReplaceColor-xHVYigNvCgefD-removebg-preview.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('imgonline-com-ua-ReplaceColor-yHH1YhmDJiwN8T-removebg-preview.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_7.collidepoint((mx, my)):
			if click:
				c.play()
				all_lap()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		screen.blit(pygame.image.load('back.png'), (10, 740))
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

def lap5():
	global click
	global backgroundmainimg
	global carmainimg
	global carconlaiimg1
	global carconlaiimg2
	global carconlaiimg3
	global carconlaiimg4
	global carconlaiimg5
	global carconlaiimg1_copy
	global carconlaiimg2_copy
	global carconlaiimg3_copy
	global carconlaiimg4_copy
	global carconlaiimg5_copy
	global carmainimg_copy
	while True:
		screen.fill((0,0,0))
		mx , my = pygame.mouse.get_pos()
		button_4img = pygame.image.load('short-lap.png')
		button_4width = button_4img.get_width()
		button_4 = screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		button_5img = pygame.image.load('medium-lap.png')
		button_5width = button_5img.get_width()
		button_5 = screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		button_6img = pygame.image.load('long-lap.png')
		button_6width = button_6img.get_width()
		button_6 = screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		button_7img = pygame.image.load('back.png')
		button_7width = button_7img.get_width()
		button_7 = screen.blit(pygame.image.load('back.png'), (10, 740))
		if button_4.collidepoint((mx, my)):
			if click:
				c.play()
				backgroundmainimg = pygame.image.load('lap5(short).jpg')
				carmainimg = pygame.image.load('131741397_150385079887557_1201017971494362165_n.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('131818741_857484225072804_2266848575272084716_n.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('131902754_711943599718339_3008432960100158975_n.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('131993666_176856580789896_746549070693015588_n.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('132304419_2675436436042945_5289629922444086631_n.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('132424209_1270510353334608_6040071931618722448_n.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_5.collidepoint((mx, my)):
			if click:
				c.play()
				backgroundmainimg = pygame.image.load('lap5(medium).jpg')
				carmainimg = pygame.image.load('131741397_150385079887557_1201017971494362165_n.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('131818741_857484225072804_2266848575272084716_n.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('131902754_711943599718339_3008432960100158975_n.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('131993666_176856580789896_746549070693015588_n.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('132304419_2675436436042945_5289629922444086631_n.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('132424209_1270510353334608_6040071931618722448_n.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_6.collidepoint((mx, my)):
			if click:
				c.play()
				backgroundmainimg = pygame.image.load('lap5(long).jpg')
				carmainimg = pygame.image.load('131741397_150385079887557_1201017971494362165_n.png')
				carmainimg_copy = pygame.transform.flip(carmainimg, True, False)
				carconlaiimg1 = pygame.image.load('131818741_857484225072804_2266848575272084716_n.png')
				carconlaiimg1_copy = pygame.transform.flip(carconlaiimg1, True, False)
				carconlaiimg2 = pygame.image.load('131902754_711943599718339_3008432960100158975_n.png')
				carconlaiimg2_copy = pygame.transform.flip(carconlaiimg2, True, False)
				carconlaiimg3 = pygame.image.load('131993666_176856580789896_746549070693015588_n.png')
				carconlaiimg3_copy = pygame.transform.flip(carconlaiimg3, True, False)
				carconlaiimg4 = pygame.image.load('132304419_2675436436042945_5289629922444086631_n.png')
				carconlaiimg4_copy = pygame.transform.flip(carconlaiimg4, True, False)
				carconlaiimg5 = pygame.image.load('132424209_1270510353334608_6040071931618722448_n.png')
				carconlaiimg5_copy = pygame.transform.flip(carconlaiimg5, True, False)
				Datcuoc()
		if button_7.collidepoint((mx, my)):
			if click:
				c.play()
				all_lap()
		screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
		screen.blit(pygame.image.load('short-lap.png'), (int(1000 - button_4width) / 2,350))
		screen.blit(pygame.image.load('medium-lap.png'), (int(1000 - button_5width) / 2,450))
		screen.blit(pygame.image.load('long-lap.png'), (int(1000 - button_6width) / 2,550))
		screen.blit(pygame.image.load('back.png'), (10, 740))
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

#car in main game	
carmain_y = 320
carmain_x = 50
carmain_speed = 3
save = 0
#car con lai
carconlai_x = 50
carconlai_speed = 3
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
#bua dung
buadungimg = pygame.image.load('buadung.png')
buadungwidth = buadungimg.get_width()
buadungheight = buadungimg.get_height()
#bua quay lai
buaquaylaiimg = pygame.image.load('back-arrow.png')
buaquaylaiwidth = buaquaylaiimg.get_width()
buaquaylaiheight = buaquaylaiimg.get_height()
#bua bat dau lai
buabatdaulaiimg = pygame.image.load('bua-bat-dau-lai.png')
buabatdaulaiwidth = buabatdaulaiimg.get_width()
buabatdaulaiheight = buabatdaulaiimg.get_height()
#backgroung thang thua 
backgroundmainimg1 = pygame.image.load('iron man/134404164_256418259236292_1122539562479276773_n.jpg')

screen = pygame.display.set_mode((640,480),RESIZABLE)
speedcar1 = random.randint(200,500)
speedcar2 = random.randint(200,500)
speedcar3 = random.randint(200,500)
speedcar4 = random.randint(200,500)
speedcar5 = random.randint(200,500)
speedcar6 = random.randint(200,500)
class BuaQuayLai():
	def __init__(self):
		self.img = buaquaylaiimg
		self.width = buaquaylaiwidth
		self.height = buaquaylaiheight
		self.speed = 5
		self.distance = 10000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   1500 + i*self.distance
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

class BuaDung():
	def __init__(self):
		self.img = buadungimg
		self.width = buadungwidth
		self.height = buadungheight
		self.speed = 1.5
		self.distance = 9000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   1200 + i*self.distance
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
			x =   11000 + i*self.distance
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
		self.distance = 9000
		self.ls = []
		self.save = 0
		for i in range(6):
			x =   1300 + i*self.distance
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

def rectcollision(rect1, rect2):
	if rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2] and rect1[1] <= rect2[1] + rect2[3] and rect2[1] <= rect1[1] + rect1[3]:
		return True
	else :return False

def chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buadichchuyen.ls[i][0]*100 + (100-buadichchuyen.width) / 2)
		x = int(buadichchuyen.ls[i][1])
		buadichchuyenRect = [x, y, buadichchuyen.width, buadichchuyen.height]
		if rectcollision(car1Rect, buadichchuyenRect):
			return 1
		elif rectcollision(car2Rect, buadichchuyenRect):
			return 2
		elif rectcollision(car3Rect, buadichchuyenRect):
			return 3
		elif rectcollision(car4Rect, buadichchuyenRect):
			return 4
		elif rectcollision(car5Rect, buadichchuyenRect):
			return 5
		elif rectcollision(car6Rect, buadichchuyenRect):
			return 6
		else :return False

def chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buanhanh.ls[i][0]*100 + (100-buanhanh.width) / 2)
		x = int(buanhanh.ls[i][1])
		buanhanhRect = [x, y, buanhanh.width, buanhanh.height]
		if rectcollision(car1Rect, buanhanhRect):
			return 1
		if rectcollision(car2Rect, buanhanhRect):
			return 2
		if rectcollision(car3Rect, buanhanhRect):
			return 3
		if rectcollision(car4Rect, buanhanhRect):
			return 4
		if rectcollision(car5Rect, buanhanhRect):
			return 5
		if rectcollision(car6Rect, buanhanhRect):
			return 6
		else: return False

def chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buacham.ls[i][0]*100 + (100-buacham.width) / 2)
		x = int(buacham.ls[i][1])
		buachamRect = [x, y, buacham.width, buacham.height]
		if rectcollision(car1Rect, buachamRect):
			return 1
		if rectcollision(car2Rect, buachamRect):
			return 2
		if rectcollision(car3Rect, buachamRect):
			return 3
		if rectcollision(car4Rect, buachamRect):
			return 4
		if rectcollision(car5Rect, buachamRect):
			return 5
		if rectcollision(car6Rect, buachamRect):
			return 6
		else: return False

def chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buadung.ls[i][0]*100 + (100 - buadung.width) / 2)
		x = int(buadung.ls[i][1])
		buadungRect = [x, y, buadung.width, buadung.height]
		if rectcollision(car1Rect, buadungRect):
			return 1
		if rectcollision(car2Rect, buadungRect):
			return 2
		if rectcollision(car3Rect, buadungRect):
			return 3
		if rectcollision(car4Rect, buadungRect):
			return 4
		if rectcollision(car5Rect, buadungRect):
			return 5
		if rectcollision(car6Rect, buadungRect):
			return 6
		else: return False

def chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buaquaylai.ls[i][0]*100 + (100-buaquaylai.width) / 2)
		x = int(buaquaylai.ls[i][1])
		buaquaylaiRect = [x, y, buaquaylai.width, buaquaylai.height]
		if rectcollision(car1Rect, buaquaylaiRect):
			return 1
		if rectcollision(car2Rect, buaquaylaiRect):
			return 2
		if rectcollision(car3Rect, buaquaylaiRect):
			return 3
		if rectcollision(car4Rect, buaquaylaiRect):
			return 4
		if rectcollision(car5Rect, buaquaylaiRect):
			return 5
		if rectcollision(car6Rect, buaquaylaiRect):
			return 6
		else: return False

def chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buavedich.ls[i][0]*100 + (100-buavedich.width) / 2)
		x = int(buavedich.ls[i][1])
		buavedichRect = [x, y, buavedich.width, buavedich.height]
		if rectcollision(car1Rect, buavedichRect):
			return 1
		elif rectcollision(car2Rect, buavedichRect):
			return 2
		elif rectcollision(car3Rect, buavedichRect):
			return 3
		elif rectcollision(car4Rect, buavedichRect):
			return 4
		elif rectcollision(car5Rect, buavedichRect):
			return 5
		elif rectcollision(car6Rect, buavedichRect):
			return 6
		else: return False

def chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai):
	car1Rect = [car1.x , car1.y, car1.width, car1.height]
	car2Rect = [car2.x , car2.y, car2.width, car2.height]
	car3Rect = [car3.x , car3.y, car2.width, car2.height]
	car4Rect = [car4.x , car4.y, car2.width, car2.height]
	car5Rect = [car5.x , car5.y, car2.width, car2.height]
	car6Rect = [car6.x , car6.y, car2.width, car2.height]
	for i in range(6):
		y = int(MARGIN + buabatdaulai.ls[i][0]*100 + (100-buabatdaulai.width) / 2)
		x = int(buabatdaulai.ls[i][1])
		buabatdaulaiRect = [x, y, buabatdaulai.width, buabatdaulai.height]
		if rectcollision(car1Rect, buabatdaulaiRect):
			return 1
		if rectcollision(car2Rect, buabatdaulaiRect):
			return 2
		if rectcollision(car3Rect, buabatdaulaiRect):
			return 3
		if rectcollision(car4Rect, buabatdaulaiRect):
			return 4
		if rectcollision(car5Rect, buabatdaulaiRect):
			return 5
		if rectcollision(car6Rect, buabatdaulaiRect):
			return 6
		else: return False

click = False

def Datcuoc():
	global click
	global tien_thuong
	tien_thuong = 0
	car1 = Carmain()
	car2 = Carconlai1()
	car3 = Carconlai2()
	car4 = Carconlai3()
	car5 = Carconlai4()
	car6 = Carconlai5()
	buaquaylai = BuaQuayLai()
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
				ChonXe(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		if button_2.collidepoint((mx, my)):
			if click:
				tien_thuong = 10000	
				ChonXe(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		if button_3.collidepoint((mx, my)):
			if click:
				tien_thuong = 25000
				ChonXe(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		if button_4.collidepoint((mx, my)):
			if click:
				tien_thuong = 50000
				ChonXe(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		if button_5.collidepoint((mx, my)):
			if click:
				tien_thuong = 100000
				ChonXe(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
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

def ChonXe(screen, car1, car2, car3, car4, car5, car6, buaquaylai):
	global click
	global xechon
	global carmainimg
	global carconlaiimg1
	global carconlaiimg2
	global carconlaiimg3
	global carconlaiimg4
	global carconlaiimg5
	car1.__init__()
	car2.__init__()
	car3.__init__()
	car4.__init__()
	car5.__init__()
	car6.__init__()
	buaquaylai.__init__()
	while True:
		s.play
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_1img = carmainimg
		button_1width = button_1img.get_width()
		button_1 = screen.blit(carmainimg, (int(1000 - button_1img.get_width()), 200))
		button_2img = carconlaiimg1
		button_2width = button_2img.get_width()
		button_2 = screen.blit(carconlaiimg1, (int(1000 - button_2img.get_width()), 270))
		button_3img = carconlaiimg2
		button_3width = button_3img.get_width()
		button_3 = screen.blit(carconlaiimg2, (int(1000 - button_3img.get_width()), 340))
		button_4img = carconlaiimg3
		button_4width = button_4img.get_width()
		button_4 = screen.blit(carconlaiimg3, (int(1000 - button_4img.get_width()), 410))
		button_5img = carconlaiimg4
		button_5width = button_5img.get_width()
		button_5 = screen.blit(carconlaiimg4, (int(1000 - button_5img.get_width()), 480))
		button_6img = carconlaiimg5
		button_6width = button_6img.get_width()
		button_6 = screen.blit(carconlaiimg5, (int(1000 - button_6img.get_width()), 550))
		if button_1.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 1
				if menuinrace.get_chon() == 1:
					carmainimg = menuinrace.get_skin()
				maingame()
		if button_2.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 2
				if menuinrace.get_chon() == 1:
					carconlaiimg1 = menuinrace.get_skin()
				maingame()
		if button_3.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 3
				if menuinrace.get_chon() == 1:
					carconlaiimg2 = menuinrace.get_skin()
				maingame()
		if button_4.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 4
				if menuinrace.get_chon() == 1:
					carconlaiimg3 = menuinrace.get_skin()
				maingame()
		if button_5.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 5
				if menuinrace.get_chon() == 1:
					carconlaiimg4 = menuinrace.get_skin()
				maingame()
		if button_6.collidepoint((mx, my)):
			if click:
				c.play()
				xechon = 6
				if menuinrace.get_chon() == 1:
					carconlaiimg5 = menuinrace.get_skin()
				maingame()
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
		screen.blit(carmainimg, (int(1000 - carmainimg.get_width()), 200))
		screen.blit(carconlaiimg1, (int(1000 - carconlaiimg1.get_width()), 270))
		screen.blit(carconlaiimg2, (int(1000 - carconlaiimg2.get_width()), 340))
		screen.blit(carconlaiimg3, (int(1000 - carconlaiimg3.get_width()), 410))
		screen.blit(carconlaiimg4, (int(1000 - carconlaiimg4.get_width()), 480))
		screen.blit(carconlaiimg5, (int(1000 - carconlaiimg5.get_width()), 550))
		pygame.display.update()
		fpsclock.tick(60)


class Save():
	def __init__(self):
		self.save = 0
	def update(self):
		self.save += (10 / 6)

class Carmain():
	def __init__(self):
		self.img = carmainimg
		self.img1 = carmainimg_copy
		self.x = 0
		self.y = carmain_y
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.speed = carmain_speed
		self.save = 0
		self.save1 = 0
		self.score = 0
		self.count = 10
	def draw(self,screen,car1, car2, car3, car4, car5, car6, buaquaylai):
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 1:
			screen.blit(self.img1,(int(self.x), int(self.y)))	
		else: 
			screen.blit(self.img,(int(self.x), int(self.y)))
	def run(self):
		self.save1 += 100
		self.save = speedcar1
		self.x += 3
		if self.x > self.save:
			self.x = self.save
		if self.save1 > backgroundmainimg.get_width() - 1000:
			self.x += 4
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
	def update(self,car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width: 
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) == 1:
			self.x += 400
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 1:
			self.x += 1010
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 1:
			self.x -= 5
		elif chamBuaNhanh(car1, car2 ,car3 , car4, car5, car6, buanhanh) == 1:
			self.x += 4
		elif chamBuaDungLai(car1, car2 ,car3 , car4, car5, car6, buadung) == 1:
			self.x += 0
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 1:
			self.x -= self.x + self.save
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 1:
			self.x -= 5
		if save.save > speedcar1 and save.save < backgroundmainimg.get_width() - 1000: 
			self.x += random.randint(-3,3)
		if save.save >= backgroundmainimg.get_width() - 1000:
			self.x += 5
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
		if save.save < speedcar1:
			self.x += 2

class Carconlai1():
	def __init__(self):
		self.img = carconlaiimg1
		self.img1 = carconlaiimg1_copy
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.speed = carconlai_speed
		self.x = 0
		self.y = 120
		self.save = 0
		self.save1 = 0
		self.score = 0
		self.count = 10
	def draw(self, screen,car1, car2, car3, car4, car5, car6, buaquaylai):
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 2:
			screen.blit(self.img1,(int(self.x), 120))
		else:
			screen.blit(self.img,(int(self.x),120 ))
	def run(self):
		self.save1 += 10
		self.save = speedcar2
		self.save1 += 10
		self.x += 3
		if self.x > self.save:
			self.x = self.save
		if self.save1 > backgroundmainimg.get_width() - 1000:
			self.x += 4
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
	def update(self, car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width: 
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) == 2:
			self.x += 400
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 2:
			self.x += 1010
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 2:
			self.x -= 5
		elif chamBuaNhanh(car1, car2 ,car3 , car4, car5, car6, buanhanh) == 2:
			self.x += 4
		elif chamBuaDungLai(car1, car2 ,car3 , car4, car5, car6, buadung) == 2:
			self.x += 0
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 2:
			self.x -= self.x + self.save
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 2:
			self.x -= 5
		if save.save > speedcar2 and save.save < backgroundmainimg.get_width() - 1000: 
			self.x += random.randint(-3,3)						
		if save.save >= backgroundmainimg.get_width() - 1000:
			self.x += 5
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
		if save.save < speedcar2:
			self.x += 2

class Carconlai2():
	def __init__(self):
		self.img = carconlaiimg2
		self.img1 = carconlaiimg2_copy
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.speed = carconlai_speed
		self.x = 0
		self.y = 220
		self.save = 0
		self.save1 = 0
		self.score = 0
		self.count = 10
	def draw(self, screen, car1, car2, car3, car4, car5, car6, buaquaylai):
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 3:
			screen.blit(self.img1,(int(self.x), 220))
		else:
			screen.blit(self.img,(int(self.x), 220))
	def run(self):
		self.save1 += 10
		self.save = speedcar3
		self.x += 3
		if self.x > self.save:
			self.x = self.save
		if self.save1 > backgroundmainimg.get_width() - 1000:
			self.x += 4
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
	def update(self,car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width: 
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) == 3:
			self.x += 400
			self.save = self.x
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 3:
			self.x += 1010
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 3:
			self.x -= 5
		elif chamBuaNhanh(car1, car2 ,car3 , car4, car5, car6, buanhanh) == 3:
			self.x += 4
		elif chamBuaDungLai(car1, car2 ,car3 , car4, car5, car6, buadung) == 3:
			self.x += 0
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 3:
			self.x -= self.x + self.save
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 3:
			self.x -= 5
		if save.save > speedcar3 and save.save < backgroundmainimg.get_width() - 1000: 
			self.x += random.randint(-3,3)
		if save.save >= backgroundmainimg.get_width() - 1000:
			self.x += 5
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
		if save.save < speedcar3:
			self.x += 2

class Carconlai3():
	def __init__(self):
		self.img = carconlaiimg3
		self.img1 = carconlaiimg3_copy
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.speed = carconlai_speed
		self.x = 0
		self.y = 420
		self.save = 0
		self.save1 = 0
		self.score = 0
		self.count  = 10
	def draw(self, screen, car1, car2, car3, car4, car5, car6, buaquaylai):
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 4:
			screen.blit(self.img1,(int(self.x), 420))
		else:
			screen.blit(self.img,(int(self.x), 420))
	def run(self):
		self.save1 += 10	 
		self.save = speedcar4
		self.x += 3
		if self.x > self.save:
			self.x = self.save
		if self.save1 > backgroundmainimg.get_width() - 1000:
			self.x += 4
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
	def update(self, car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width: 
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) == 4:
			self.x += 400
			self.save = self.x
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 4:
			self.x += 1010
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 4:
			self.x -= 5
		elif chamBuaNhanh(car1, car2 ,car3 , car4, car5, car6, buanhanh) == 4:
			self.x += 4
		elif chamBuaDungLai(car1, car2 ,car3 , car4, car5, car6, buadung) == 4:
			self.x += 0
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 4:
			self.x -= self.x + self.save
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 4:
			self.x -= 5
		if save.save > speedcar4 and save.save < backgroundmainimg.get_width() - 1000: 
			self.x += random.randint(-3,3)
		if save.save > backgroundmainimg.get_width() - 1000:
			self.x += 5
			if self.x >= 1000 - self.width:
				self.x = 1000 - self.width
		if save.save < speedcar4:
			self.x += 2


class Carconlai4():
	def __init__(self):
		self.img = carconlaiimg4
		self.img1 = carconlaiimg4_copy
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.speed = carconlai_speed
		self.x = 0
		self.y = 520
		self.save = 0
		self.save1 = 0
		self.score = 0
		self.count = 10
	def draw(self, screen, car1, car2, car3, car4, car5, car6, buaquaylai):
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 5:
			screen.blit(self.img1,(int(self.x), 520))
		else:
			screen.blit(self.img,(int(self.x), 520))
	def run(self):
		self.save1 += 10
		self.save = speedcar5
		self.x += 3
		if self.x > self.save:
			self.x = self.save 
		if self.save1 > backgroundmainimg.get_width() - 1000:
			self.x += 4
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
	def update(self, car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save):   
		save.update()
		self.save += 10
		if self.x < 1000 - self.width: 
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) == 5:
			self.x += 400
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 5:
			self.x += 1010
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 5:
			self.x -= 5
		elif chamBuaNhanh(car1, car2 ,car3 , car4, car5, car6, buanhanh) == 5:
			self.x += 4
		elif chamBuaDungLai(car1, car2 ,car3 , car4, car5, car6, buadung) == 5:
			self.x += 0
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 5:
			self.x -= self.x + self.save
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 5:
			self.x -= 5
		if save.save > speedcar5 and save.save < backgroundmainimg.get_width() - 1000: 
			self.x += random.randint(-3,3)
		if save.save >= backgroundmainimg.get_width() - 1000:
			self.x += 5
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
		if save.save < speedcar5:
			self.x += 2


class Carconlai5():
	def __init__(self):
		self.img = carconlaiimg5
		self.img1 = carconlaiimg5_copy
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.speed = carconlai_speed
		self.x = 0
		self.y = 620 
		self.save = 0
		self.save1 = 0
		self.score = 0
		self.count = 10
	def draw(self, screen, car1, car2, car3, car4, car5, car6, buaquaylai):
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 6:
			screen.blit(self.img1,(int(self.x), 620))
		else:
			screen.blit(self.img,(int(self.x), 620))
	def run(self):
		self.save1 += 10
		self.save = speedcar6
		self.x += 3
		if self.x > self.save:
			self.x = self.save
		if self.save1 > backgroundmainimg.get_width() - 1000:
			self.x += 4
			if self.x > 1000 - self.width:
				self.x = 1000 -self.width
	def update(self, car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save):
		save.update()
		self.save += 10
		if self.x < 1000 - self.width: 
			self.score += 0.1
		else: self.score += 0
		if self.x >= 1000 - self.width:
			self.count = 0
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) == 6:
			self.x += 400
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 6:
			self.x += 1010
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 6:
			self.x -= 5
		elif chamBuaNhanh(car1, car2 ,car3 , car4, car5, car6, buanhanh) == 6:
			self.x += 4
		elif chamBuaDungLai(car1, car2 ,car3 , car4, car5, car6, buadung) == 6:
			self.x += 0
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 6:
			self.x -= self.x + self.save
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 6:
			self.x -= 5
		if save.save > speedcar6 and save.save < backgroundmainimg.get_width() - 1000: 
			self.x += random.randint(-3,3)
		if save.save >= backgroundmainimg.get_width() - 1000:
			self.x += 5
			if self.x > 1000 - self.width:
				self.x = 1000 - self.width
		if save.save < speedcar6:
			self.x += 2

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
	def update(self,car1, car2, car3, car4, car5, car6):
		self.save += 10	
		self.x -= self.speed
		if self.save > self.width - 1000:
			self.speed = 0

		
click = False

def gamestart(bg, car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich,buacham,buanhanh,buadung, buabatdaulai, buaquaylai, save, screen):
	global click
	global angle 
	bg.__init__()
	car1.__init__()
	car2.__init__()
	car3.__init__()
	car4.__init__()
	car5.__init__()
	car6.__init__()
	buadichchuyen.__init__()
	buavedich.__init__()
	buacham.__init__()
	buanhanh.__init__()
	buadung.__init__()
	buabatdaulai.__init__()
	buaquaylai.__init__()
	save.__init__()
	angle = 0
	while True:
		angle += 1
		s.play()
		screen.fill((0,0,0))
		mx, my = pygame.mouse.get_pos()
		button_4 = screen.blit(pygame.image.load('button-exit.png'), (10,700))
		button_4img = pygame.image.load('button-exit.png')
		button_4width = button_4img.get_width()	
		button_5 = screen.blit(pygame.image.load('back.png'), (10, 740))
		button_5img = pygame.image.load('back.png')
		if button_5.collidepoint((mx, my)):
			if click:
				w.stop()
				all_lap()
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
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen) != False:
			s.stop()
			t.play()
		if chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) != False:
			s.stop()
			t.play()
		if chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) != False:
			s.stop()
			t.play()
		if chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) != False:
			s.stop()
			t.play()
		if chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) != False:
			s.stop()
			t.play()
		if chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) != False:
			s.stop()
			t.play()
		if chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) != False:
			s.stop()
			t.play()
		bg.draw(screen)
		bg.update(car1, car2, car3, car4, car5, car6)
		
		car1.draw(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		car2.draw(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		car3.draw(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		car4.draw(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		car5.draw(screen, car1, car2, car3, car4, car5, car6, buaquaylai)
		car6.draw(screen, car1, car2, car3, car4, car5, car6, buaquaylai)

		car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)

		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen)==1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 1:
			car1.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)

		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen)==2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) == 2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) == 2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 2:
			car2.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen)==3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) == 3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) == 3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 3:
			car3.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen)==4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) == 4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) == 4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 4:
			car4.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen)==5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) == 5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) == 5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 5:
			car5.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
			
		if chamBuadichchuyen(car1, car2, car3, car4, car5, car6, buadichchuyen)==6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaVeDich(car1, car2, car3, car4, car5, car6, buavedich) == 6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaLamCham(car1, car2, car3, car4, car5, car6, buacham) == 6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaNhanh(car1, car2, car3, car4, car5, car6, buanhanh) == 6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh,buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaDungLai(car1, car2, car3, car4, car5, car6, buadung) == 6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaBatDauLai(car1, car2, car3, car4, car5, car6, buabatdaulai) == 6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
		elif chamBuaQuayLai(car1, car2, car3, car4, car5, car6, buaquaylai) == 6:
			car6.update(car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich, buacham, buanhanh, buadung, buabatdaulai, buaquaylai, save)
				
		buacham.drawinmaingame(screen)
		buacham.update()

		buanhanh.drawinmaingame(screen)
		buanhanh.update()

		buadichchuyen.drawinmaingame(screen)
		buadichchuyen.update()

		buavedich.drawinmaingame(screen)
		buavedich.update()

		buabatdaulai.drawinmaingame(screen)
		buabatdaulai.update()
		
		buaquaylai.drawinmaingame(screen)
		buaquaylai.update()

		if car1.count + car2.count + car3.count + car4.count + car5.count + car6.count == 0	:
			screen.blit(backgroundmainimg1, (0,0))
			screen.blit(button_5img, (10, 740))
			s.stop()
			w.play()
			if car1.score == min(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score):
				screen.blit(pygame.transform.rotate(car1.img, angle), (int(1000 - car1.width) / 2, 330))
				if xechon == 1:
					menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong * 2)
			elif car1.score == max(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score) and xechon == 1:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien() - tien_thuong)
			else:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong)
			if car2.score == min(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score):
				screen.blit(pygame.transform.rotate(car2.img, angle), (int(1000 - car2.width) 	/ 2, 330))
				if xechon == 2:
					menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong * 2)
			elif car2.score == max(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score) and xechon == 2:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien() - tien_thuong)
			else:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong)
			if car3.score == min(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score):
				screen.blit(pygame.transform.rotate(car3.img, angle), (int(1000 - car3.width) / 2, 330))
				if xechon == 3:
					menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong * 2)
			elif car3.score == max(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score) and xechon == 3:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien() - tien_thuong)
			else:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong)
			if car4.score == min(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score):
				screen.blit(pygame.transform.rotate(car4.img, angle), (int(1000 - car4.width) / 2, 330))
				if xechon == 4:
					menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong * 2)
			elif car4.score == max(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score) and xechon == 4:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien() - tien_thuong)
			else:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong)
			if car5.score == min(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score):
				screen.blit(pygame.transform.rotate(car5.img, angle), (int(1000 - car5.width) / 2, 330))
				if xechon == 5:
					menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong * 2)
			elif car5.score == max(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score) and xechon == 5:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien() - tien_thuong)
			else:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong)
			if car6.score == min(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score):
				screen.blit(pygame.transform.rotate(car6.img, angle), (int(1000 - car6.width) / 2, 330))
				if xechon == 6:
					menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong * 2)
			elif car6.score == max(car1.score, car2.score, car3.score, car4.score, car5.score, car6.score) and xechon == 6:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien() - tien_thuong)
			else:
				menuinrace.save_data(menuinrace.get_name(),menuinrace.get_tien()+tien_thuong)
	
		pygame.display.update()
		fpsclock.tick(120)

def maingame():
	bg = backgroundamin()
	car1 = Carmain()
	car2 = Carconlai1()
	car3 = Carconlai2()
	car4 = Carconlai3()
	car5 = Carconlai4()
	car6 = Carconlai5()
	buadichchuyen = BuaDichChuyen()
	buavedich = BuaVeDich()
	buacham = BuaCham()
	buanhanh = BuaNhanh()
	buadung = BuaDung()
	buaquaylai = BuaQuayLai()
	buabatdaulai = BuaBatDauLai()
	buaquaylai = BuaQuayLai()
	save = Save()
	screen = pygame.display.set_mode((1000,800))
	while True:
		gamestart(bg, car1, car2, car3, car4, car5, car6, buadichchuyen, buavedich,buacham,buanhanh,buadung,buabatdaulai,buaquaylai, save, screen)

