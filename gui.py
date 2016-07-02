import sys, pygame, random, time, datetime
from pygame.locals import *
from time import strftime, gmtime
import datetime

class Image:
	def __init__(self, image, x, y):
		self.x = x
		self.y = y
		self.image = pygame.image.load(image)
		self.coords = (x,y)
		self.rect = self.image.get_rect()
		self.width = self.image.get_width()
		self.height = self.image.get_height()
	
	def draw(self, DS):
		DS.blit(self.image, self.coords)

class Text:
	def __init__(self, text, x, y, font, size, color=None):
		self.x = x
		self.y = y
		self.coords = (x, y)
		self.text = text
		self.size = size
		self.font = pygame.font.Font(font, size)
		
		if color == None:
			self.color = (0,0,0)
		else:
			self.color = color

		self.render = self.font.render(self.text, True, self.color)
		self.rect = self.render.get_rect()
		self.height = self.rect.height
		self.width = self.rect.width

	def draw(self, DS):
		self.render = self.font.render(self.text, True, self.color)
		DS.blit(self.render, self.coords)

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

	background = Image('Background.png', 0, 0)
	topbar = Image('TopLine.png', 0, 0)
	bottombar = Image('BottomLine.png', 0, 408)
	clockImg = Image('Clock.png', 395, 61)
	media = Image('MediaButton.png', 24, 112)
	button = Image('LargeButton.png', 24, 204)
	button2 = Image('LargeButton.png', 24, 296)
	minutehand = Image('MinuteHand.png', 395, 61)
	hourhand = Image('HourHand.png', 395, 61)

	hour = Text(strftime('%I'), 675, 412, 'freesansbold.ttf', 60, (0,0,0))
	minutes = Text(strftime('%M'), 740, 412, 'freesansbold.ttf', 29, (0,0,0))
	date = Text(strftime("%A, %B %d, %Y"), 10, 430, 'freesansbold.ttf', 36, (0,0,0))
	ampm = Text(strftime("%p"), 740, 437, 'freesansbold.ttf', 29, (0,0,0))
	
	mousex = 0
	mousey = 0
	mouseclicked = False
	
	while True:
		
		csecond = datetime.datetime.now().second
		cminute = minutes.text = datetime.datetime.now().minute
		chour = datetime.datetime.now().hour
		rot_minutehand = rot_center(minutehand.image, (360.0-((6.0*cminute)+(.1*csecond))))
		rot_hourhand = rot_center(hourhand.image, (360.0-((.5*cminute)+(30.0*chour))))
		
		hour.text = strftime('%I')
		minutes.text = strftime('%M')
		ampm.text = strftime("%p")
		date.text = strftime("%A, %B %d, %Y")
		
		background.draw(DS)
		topbar.draw(DS)
		bottombar.draw(DS)
		clockImg.draw(DS)
		media.draw(DS)
		button.draw(DS)
		button2.draw(DS)
		DS.blit(rot_minutehand, (395,61))
		DS.blit(rot_hourhand, (395,61))
		hour.draw(DS)
		minutes.draw(DS)
		ampm.draw(DS)
		date.draw(DS)
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
