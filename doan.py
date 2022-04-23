import pygame, sys
from pygame.locals import*
import minigame
import maingame
from tkinter import*
import menuinrace

pygame.init()
fpsclock = pygame.time.Clock()
global NameinGame

def draw_text(text, font , color, surface, x, y):                                        
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y) 
	surface.blit(textobj, textrect)	
click = False


def register(): x
  global screen_register
  screen_register = Toplevel(screen_main)
  screen_register.title("Register")
  screen_register.geometry("800x500")
  global username_r
  global password_r
  global username_entry_r
  global password_entry_r
  username_r = StringVar()
  password_r = StringVar()

  bg=PhotoImage(file="login.png")
  my_lable= Label(screen_register,image = bg)
  my_lable.place(x=0,y=0,relwidth=1,relheight=1)
  
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "Please enter details below").pack()
  Label(screen_register, text = "").pack()
  Label(screen_register, text = "Username * ").pack()
  username_entry_r = Entry(screen_register, textvariable = username_r)
  username_entry_r.pack()
  Label(screen_register, text = "Password * ").pack()
  password_entry_r =  Entry(screen_register, textvariable = password_r)
  password_entry_r.pack()
  Label(screen_register, text = "").pack()
  Button(screen_register, text = "Register", width = 10, height = 1, command = register_user).pack()
  screen_register.mainloop()

def register_user():  

  username_info_r = username_entry_r.get()
  password_info_r = password_entry_r.get()

  file=open(username_info_r+".txt", "a+")
  file.write(username_info_r+"\n")
  file.write(password_info_r+"\n")
  file.write("10000\n")
  file.close()

  file = open("listname.txt","a+")
  file.write(username_info_r+"\n")
  file.close()

  username_entry_r.delete(0, END)
  password_entry_r.delete(0, END)

  Label(screen_register, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()
  
def checkUserInList():
  file = open("listname.txt","r")
  check=file.readlines(0)
  file.close()
  for i in range(len(check)):
    if  tk==check[i].strip():
      kt=True
      break
    else :
      kt=False
  return kt   


def check_login():
  global Nameingame 
  global tk
  tk=username_entry.get()
  mk=password_entry.get()
  if checkUserInList()==True:
    file = open(tk+".txt","r")
    line=file.readlines(0)
    file.close()
    if line[0].strip() == tk:
      if line[1].strip() == mk:
        check = True
      else:
        check = False  
    else:
        check = False
    if check == False :
      Label(screen_login, text = "Login Fail (Wrong Password)", fg = "green" ,font = ("calibri", 11)).pack()
    else:
      screen_login.destroy()
      screen_main.destroy()
      maingame.get_name(tk)
      menuinrace.racemenu(tk)
  else:
    Label(screen_login, text = "Not exist Username", fg = "green" ,font = ("calibri", 11)).pack()


def login():
  global screen_login
  screen_login = Toplevel(screen_main)
  screen_login.title("Login")
  screen_login.geometry("800x500")
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  bg=PhotoImage(file="login.png")
  my_lable= Label(screen_login,image = bg)
  my_lable.place(x=0,y=0,relwidth=1,relheight=1)

  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "Please enter details below").pack()
  Label(screen_login, text = "").pack()
  Label(screen_login, text = "Username * ").pack()
  username_entry = Entry(screen_login, textvariable = username)
  username_entry.pack()
  Label(screen_login, text = "Password * ").pack()
  password_entry =  Entry(screen_login, textvariable = password)
  password_entry.pack()
  Label(screen_login, text = "").pack()
  Button(screen_login, text = "Login", width = 10, height = 1, command = check_login).pack()
  screen_login.mainloop()


def main_screen():
  global screen_main
  screen_main = Tk()
  screen_main.geometry("800x500")
  screen_main.title("Race car")

  bg=PhotoImage(file="login.png")
  my_lable= Label(screen_main,image = bg)
  my_lable.place(x=0,y=0,relwidth=1,relheight=1)

  Label(text = "").pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register",height = "2", width = "30", command = register).pack()
  screen_main.mainloop()

def main_mennu():
    s=pygame.mixer.Sound("tokyo_drift.mp3")
    m = pygame.mixer.Sound("move.wav")
    WINDOWWIGTH = 1000
    WINDOWHEIGHT = 800
    screen = pygame.display.set_mode((WINDOWWIGTH,WINDOWHEIGHT))
    pygame.display.set_caption('DO AN CUOI KY') 
    font = pygame.font.SysFont('Colonna MT', 100)
    screen = pygame.display.set_mode((1000,800),RESIZABLE)
    global click
    t=0
    while True: 
      if t!=1:
        s.play()
        t=1
      screen.fill((0,0,0))
      mx, my = pygame.mouse.get_pos()
      button_1img = pygame.image.load('start-button.png') 
      button_1width = button_1img.get_width()
      button_1 = screen.blit(pygame.image.load('start-button.png'), (int(1000 - button_1width) / 2,350))
      button_3img = pygame.image.load('about-button.png')
      button_3width = button_3img.get_width()
      button_3 = screen.blit(pygame.image.load('about-button.png'), (int(1000 - button_1width) / 2,450))
      button_4 = screen.blit(pygame.image.load('button-exit.png'), (10,700))
      button_4img = pygame.image.load('button-exit.png')
      button_4width = button_4img.get_width()	
      button_5img = pygame.image.load('menu.png')
      button_5width = button_5img.get_width()	
      button_5 = screen.blit(pygame.image.load('menu.png'), (int(1000 - button_5width) / 2,150))  
      
      if button_1.collidepoint((mx, my)):
        if click:
          m.play()
          main_screen()
      if button_4.collidepoint((mx, my)):
        if click:
          sys.exit()
          
      screen.blit(pygame.image.load('background-menu.jpg'), (0,0))
      screen.blit(pygame.image.load('menu.png'), (int(1000 - button_5width) / 2,150))
      screen.blit(pygame.image.load('start-button.png'), (int(1000 - button_1width) / 2,350))
      screen.blit(pygame.image.load('about-button.png'), (int(1000 - button_1width) / 2,450))
      screen.blit(pygame.image.load('button-exit.png'), (10,700))
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

main_mennu()