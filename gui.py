import sys, pygame, random, time, datetime, mutagen, os
from pygame.locals import *
from time import strftime, gmtime
from datetime import datetime
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3

class Image:
	def __init__(self, image, x, y, clickable = False, action = None):
		self.x = x
		self.y = y
		self.image = pygame.image.load(image)
		self.coords = (x,y)
		self.rect = self.image.get_rect()
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.clickable = clickable
		self.action = action
	
	def draw(self, DS):
		DS.blit(self.image, self.coords)
	
	def checkclick(self, mousex, mousey):
		return (self.y+self.height > mousey > self.y and 
				self.x+self.width > mousex > self.x)

class Text:
	def __init__(self, text, x, y, font, size, color=None, clickable = False, action = None):
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
		self.clickable = clickable
		self.action = action

	def draw(self, DS):
		self.render = self.font.render(self.text, True, self.color)
		DS.blit(self.render, self.coords)

class Sound:
	def __init__(self, sound):
		self.sound = sound

class Panel:
	def __init__(self):
		self.start = []
		self.media = []
	
	def to_start(self):
		self.current = self.start

	def to_media(self):
		self.current = self.media

def quit():
	pygame.quit()
	sys.exit()

def playsong():
	pygame.mixer.music.stop()
	pygame.mixer.music.load('testsong.mp3')
	pygame.mixer.music.play()

def stopsong():
	pygame.mixer.music.stop()

def rot_center(image, angle):
	#"""rotate an image while keeping its center and size"""
	orig_rect = image.get_rect()
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = orig_rect.copy()
	rot_rect.center = rot_image.get_rect().center
	rot_image = rot_image.subsurface(rot_rect).copy()
	return rot_image

def getsonglist():
	songs = []
	for file_ in os.listdir(os.getcwd()):
		end = file_.endswith
		if end(".mp3") or end(".wav") or end(".flac") or end(".ogg"):
			songs.append(file_)
	return sorted(songs, key=str.lower)

def gui():

	SCREENWIDTH = 800
	SCREENHEIGHT = 480
	FULLSCREEN = False

	P = Panel()
	
	pygame.init()
	FPS = 60
	fpsClock  = pygame.time.Clock()
	if FULLSCREEN:
		DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
	else:
		DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

	pygame.display.set_caption('Pi-Board')
	
	background = Image('Background.png', 0, 0)
	topbar = Image('TopLine.png', 0, 0)
	bottombar = Image('BottomLine.png', 0, 408)
	clockImg = Image('Clock2.png', 395, 61)
	media = Image('MediaButton.png', 24, 112, True, P.to_media)
	button = Image('LargeButton.png', 24, 204, True, quit)
	button2 = Image('LargeButton.png', 24, 296)
	button3 = Image('LargeButton.png', 24, 296, True, P.to_start)
	minutehand = Image('MinuteHand.png', 395, 60)
	hourhand = Image('HourHand.png', 395, 60)
	rot_minutehand = Image('MinuteHand.png', 395, 60)
	rot_hourhand = Image('HourHand.png', 395, 60)
	playbutton = Image('Play.png', 450, 300, True, playsong)
	stopbutton = Image('Stop.png', 340, 300, True, stopsong)

	hour = Text(strftime('%I'), 675, 412, 'freesansbold.ttf', 60, (0,0,0))
	minutes = Text(strftime('%M'), 740, 412, 'freesansbold.ttf', 29, (0,0,0))
	date = Text(strftime("%A, %B %d, %Y"), 10, 440, 'freesansbold.ttf', 36, (0,0,0))
	ampm = Text(strftime("%p"), 740, 437, 'freesansbold.ttf', 29, (0,0,0))
	
	P.start = [background, topbar, bottombar, clockImg, media, button, button2,
				rot_minutehand, rot_hourhand, hour, minutes, date, ampm]
	P.media = [background, bottombar, button, button3, playbutton, 
				stopbutton, hour, minutes, date, ampm]
	P.to_start()
	
	songlist = getsonglist()
	
	print (songlist)

	mousex = 0
	mousey = 0
	mouseclicked = False
	
	while True:

		now = datetime.now()
		rot_minutehand.image = rot_center(minutehand.image,
								(360.0-((6.0*now.minute)+(.1*now.second))))
		rot_hourhand.image = rot_center(hourhand.image,
								(360.0-((.5*now.minute)+(30.0*now.hour))))
		
		hour.text = strftime('%I')
		minutes.text = strftime('%M')
		ampm.text = strftime("%p")
		date.text = strftime("%A, %B %d, %Y")
		
		for obj in P.current:
			obj.draw(DS)
		
		for event in pygame.event.get():
			if event.type == QUIT:
				quit()
			elif event.type == MOUSEMOTION:
				mousex, mousey = event.pos
			elif event.type == MOUSEBUTTONDOWN:
				mouseclicked = True
			elif event.type == MOUSEBUTTONUP:
				mouseclicked = False
		
		if mouseclicked == True:
			for obj in P.current:
				if obj.clickable and obj.checkclick(mousex, mousey):
					obj.action()

		mouseclicked == False
		pygame.display.update()
		fpsClock.tick(FPS)

print gui()
