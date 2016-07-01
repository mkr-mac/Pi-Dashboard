import sys, pygame, random, time, datetime
from pygame.locals import *
from time import strftime, gmtime
import datetime

class ImageButton:
	def __init__(self, image, x, y):
		self.x = x
		self.y = y
		self.image = pygame.image.load(image)
		self.coords = (x,y)
		self.rect = self.image.get_rect()
		self.width = self.image.get_width()
		self.height = self.image.get_height()

class Text:
	def __init__(self, text, size, x, y, font=None, color=None):
		self.x = x
		self.y = y
		self.text = text
		self.size = size
		if font == None:
			self.font = pygame.font.Font('comicsansms')
		else:
			self.font = pygame.font.Font(font)
		
		if color == None:
			self.color = (0,0,0)
		else:
			self.color = color

		self.render = self.font.render(
		self.rect = self.text.get_rect()

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
	media = ImageButton('MediaButton.png', 24, 112)
	button = pygame.image.load('LargeButton.png')
	minutehand = pygame.image.load('MinuteHand.png')
	hourhand = pygame.image.load('HourHand.png')

	hour = Text('%I', 60, 675, 430, 'freesansbold.ttf', (255, 0, 0))
	fontmin = pygame.font.Font('freesansbold.ttf', 29)
	fontdate = pygame.font.SysFont('comicsansms', 37)
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

		hour.text = fonthour.render(strftime("%I"), True, hour.color)
		minutes = fontmin.render(strftime("%M"), True, (0,0,0))
		ampm = fontmin.render(strftime("%p"), True, (0,0,0))
		date = fontdate.render(strftime("%A, %B %d, %Y"), True, (0,0,0))
		
		DS.blit(background, (0,0))
		DS.blit(topbar, (0,0))
		DS.blit(bottombar, (0,408))
		DS.blit(clockImg, (395,61))
		DS.blit(media.image, media.coords)
		DS.blit(button, (24,204))
		DS.blit(button, (24,296))
		DS.blit(rot_minutehand, (395,61))
		DS.blit(rot_hourhand, (395,61))
		DS.blit(hour.text, hour.rect)
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
		
		if (media.y + media.height) > mousey > media.y and (media.x + media.width) > mousex > media.x and mouseclicked == True:
			pygame.mixer.music.stop()
			pygame.mixer.music.load('testsong.mp3')
			pygame.mixer.music.play()

		mouseclicked == False
		pygame.display.update()
		fpsClock.tick(FPS)

print gui()
