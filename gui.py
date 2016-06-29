import sys, pygame, random, time
from pygame.locals import *
from time import strftime, gmtime

def gui():
	pygame.init()

	FPS = 60
	fpsClock  = pygame.time.Clock()
	

	DS = pygame.display.set_mode((800,480))
	pygame.display.set_caption('Gooey')

	background = pygame.image.load('Background.png')
	topbar = pygame.image.load('TopLine.png')
	bottombar = pygame.image.load('BottomLine.png')
	clockImg = pygame.image.load('Clock.png')
	media = pygame.image.load('MediaButton.png')
	button = pygame.image.load('LargeButton.png')
	print (media.get_rect().size)
	
	pygame.mixer.music.load('testsong.mp3')
	pygame.mixer.music.play()
	
	fonttime = pygame.font.Font('freesansbold.ttf', 57)
	fontdate = pygame.font.Font('freesansbold.ttf', 37)
	time = fonttime.render(strftime("%I:%M"), True, (0,0,0))
	timeRect = time.get_rect()
	timeRect.center = (725, 450)
	date = fontdate.render(strftime("%m-%d-%Y"), True, (0,0,0))
	dateRect = date.get_rect()
	dateRect.center = (100, 461)
	
	while True:
		time = fonttime.render(strftime("%I:%M"), True, (0,0,0))
		date = fontdate.render(strftime("%m-%d-%Y"), True, (0,0,0))
		DS.blit(background, (0,0))
		DS.blit(topbar, (0,0))
		DS.blit(bottombar, (0,408))
		DS.blit(clockImg, (395,61))
		DS.blit(media, (24,112))
		DS.blit(button, (24,204))
		DS.blit(button, (24,296))
		DS.blit(time, timeRect)
		DS.blit(date, dateRect)
		
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

print(gui())
