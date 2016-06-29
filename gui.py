import sys, pygame, random, time, datetime
from pygame.locals import *
from time import strftime, gmtime
import datetime

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
	minloc = minutehand.get_rect().center

	pygame.mixer.music.load('testsong.mp3')
	pygame.mixer.music.play()

	fonttime = pygame.font.Font('freesansbold.ttf', 57)
	fontdate = pygame.font.Font('freesansbold.ttf', 37)
	times = fonttime.render(strftime("%I:%M"), True, (0,0,0))
	timeRect = times.get_rect()
	timeRect.center = (725, 450)
	date = fontdate.render(strftime("%m-%d-%Y"), True, (0,0,0))
	dateRect = date.get_rect()
	dateRect.center = (100, 461)
	cminuteOLD = -1
	while True:
		
		cminute = datetime.datetime.now().minute
		rot_minutehand = pygame.transform.rotate(minutehand, (360-(6*cminute)))
		rot_minutehand.get_rect().center = minloc

		times = fonttime.render(strftime("%I:%M"), True, (0,0,0))
		date = fontdate.render(strftime("%m-%d-%Y-%S"), True, (0,0,0))
		
		DS.blit(background, (0,0))
		DS.blit(topbar, (0,0))
		DS.blit(bottombar, (0,408))
		DS.blit(clockImg, (395,61))
		DS.blit(media, (24,112))
		DS.blit(button, (24,204))
		DS.blit(button, (24,296))
		DS.blit(rot_minutehand, (395,61))
		DS.blit(times, timeRect)
		DS.blit(date, dateRect)
		#150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
			elif event.type == MOUSEBUTTONDOWN:
				mousex, mousey = event.pos
			elif event.type == MOUSEBUTTONUP:
				mouseclicked = True
	
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
