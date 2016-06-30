import sys, pygame, random, time, datetime
from pygame.locals import *
from time import strftime, gmtime
import datetime

def rot_center(image, angle):
	#"""rotate an image while keeping its center and size"""
	orig_rect = image.get_rect()
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = orig_rect.copy()
	rot_rect.center = rot_image.get_rect().center
	rot_image = rot_image.subsurface(rot_rect).copy()
	return rot_image

def gui():

	SCREENWIDTH = 800
	SCREENHEIGHT = 480
	
	pygame.init()
	now = datetime.datetime.now()

	FPS = 60
	fpsClock  = pygame.time.Clock()


	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
	pygame.display.set_caption('Gooey')

	background = pygame.image.load('Background.png')
	topbar = pygame.image.load('TopLine.png')
	bottombar = pygame.image.load('BottomLine.png')
	clockImg = pygame.image.load('Clock.png')
	media = pygame.image.load('MediaButton.png')
	button = pygame.image.load('LargeButton.png')
	minutehand = pygame.image.load('MinuteHand.png')
	hourhand = pygame.image.load('HourHand.png')
	minloc = minutehand.get_rect().center

	fonthour = pygame.font.Font('freesansbold.ttf', 60)
	fontmin = pygame.font.Font('freesansbold.ttf', 29)
	fontdate = pygame.font.Font('freesansbold.ttf', 37)
	hour = fonthour.render(strftime("%I"), True, (0,0,0))
	hourRect = hour.get_rect()
	hourRect.center = (695, 450)
	minutes = fontmin.render(strftime("%M"), True, (0,0,0))
	minutesRect = minutes.get_rect()
	minutesRect.center = (745, 438)
	ampm = fontmin.render(strftime("%p"), True, (0,0,0))
	ampmRect = ampm.get_rect()
	ampmRect.topleft = (749, 462)
	date = fontdate.render(strftime("%m-%d-%Y"), True, (0,0,0))
	dateRect = date.get_rect()
	dateRect.center = (100, 461)
	
	mousex = 0
	mousey = 0
	mouseclicked = False
	
	while True:
		
		csecond = datetime.datetime.now().second
		cminute = datetime.datetime.now().minute
		chour = datetime.datetime.now().hour
		rot_minutehand = rot_center(minutehand, (360.0-((6.0*cminute)+(.1*csecond))))
		rot_hourhand = rot_center(hourhand, (360.0-((.5*cminute)+(30.0*chour))))

		hour = fonthour.render(strftime("%I"), True, (0,0,0))
		minutes = fontmin.render(strftime("%M"), True, (0,0,0))
		ampm = fontmin.render(strftime("%p"), True, (0,0,0))
		date = fontdate.render(strftime("%A, %B %d, %Y"), True, (0,0,0))
		
		DS.blit(background, (0,0))
		DS.blit(topbar, (0,0))
		DS.blit(bottombar, (0,408))
		DS.blit(clockImg, (395,61))
		DS.blit(media, (24,112))
		DS.blit(button, (24,204))
		DS.blit(button, (24,296))
		DS.blit(rot_minutehand, (395,61))
		DS.blit(rot_hourhand, (395,61))
		DS.blit(hour, hourRect)
		DS.blit(minutes, minutesRect)
		DS.blit(ampm, ampmRect)
		DS.blit(date, dateRect)
		#150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
			elif event.type == MOUSEBUTTONDOWN:
				mouseclicked = True
			elif event.type == MOUSEBUTTONUP:
				mouseclicked = False
		
		medrect = media.get_rect()
		if medrect.bottom > mousey > medrect.top and medrect.right > mousex > medrect.left and mouseclicked == True:
			pygame.mixer.music.stop()
			pygame.mixer.music.load('testsong.mp3')
			pygame.mixer.music.play()

		mouseclicked == False
		pygame.display.update()
		fpsClock.tick(FPS)

def menucontent(menu):
	if menu == START:
		return

def rectangleObject(obj, cx, cy):
	image = obj
	x = cx
	y = cy
	coords = (x,y)
	rect = obj.get_rect()

print gui()
