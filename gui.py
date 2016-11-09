import sys, pygame, random, os
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
		
	def set_coords(self, xy):
		self.coords = xy
	
	def checkclick(self, mousex, mousey):
		return (self.y+self.height > mousey > self.y and 
				self.x+self.width > mousex > self.x)

class Sound:
	def __init__(self, sound):
		self.sound = sound
		
class ScrollingList:
	def __init__(self, string_list, x, y, width, height, blocks_to_display):
		self.string_list = ['Uno', 'dos', 'tres']
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.blocks_to_display = blocks_to_display
		self.block_height = height/blocks_to_display
		self.current_block = 0
		self.clickable = True
		self.text_boxes = []
		self.action = ''
		
		for str in self.string_list:
			str = Text(str, 0, 0, 'freesansbold.ttf',32, (255,255,255), True, 'set_current_song')
			str.width = self.width
			str.height = self.height
			self.text_boxes.append(str)
		
	def draw(self, DS):
		for block in range(self.current_block, self.current_block + self.blocks_to_display):
			self.text_boxes[self.current_block+block].set_coords((self.x, self.y+block*self.block_height))
			self.text_boxes[self.current_block+block].draw(DS)
	
	def checkclick(self, mousex, mousey):
		for block in range(self.current_block, self.current_block + self.blocks_to_display):
			gl_num = self.current_block + block
			if (self.y+(block+1)*self.block_height > mousey > self.y and self.x+self.width > mousex > self.x):
				self.action = self.text_boxes[self.current_block+block].action
				return True
		return False

def quit():
	pygame.quit()
	sys.exit()

def play_song():
	pygame.mixer.music.stop()
	pygame.mixer.music.load(songlist[current_song])
	pygame.mixer.music.play()

def set_current_song():
	current_song = getsonglist()[gl_num]
	print gl_num
	return ''
	
def stop_song():
	pygame.mixer.music.stop()

def rot_center(image, angle):
	"""rotate an image while keeping its center and size"""
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

def action(action):
	if action == 'play_song':
		pygame.mixer.music.stop()
		pygame.mixer.music.load(songlist[current_song])
		pygame.mixer.music.set_volume(volume/30.0)
		pygame.mixer.music.play()
	elif action == 'stop_song':
		pygame.mixer.music.stop()
	elif action == 'next_song':
		pygame.mixer.music.stop()
		pygame.mixer.music.load(songlist[current_song])
		pygame.mixer.music.set_volume(volume)
		pygame.mixer.music.play()

SCREENWIDTH = 800
SCREENHEIGHT = 480
FULLSCREEN = False

pygame.init()
FPS = 60
fpsClock  = pygame.time.Clock()
if FULLSCREEN:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
else:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption('Pi-Board')

songlist = getsonglist()
current_song = 1
print(len(songlist))
volume = 30.0
music_paused = False

background = Image('Background.png', 0, 0)
vol_up = Image('Volume Up.png', 15, 7, True, 'volume_up')
vol_down = Image('Volume Down.png', 15, 364, True, 'volume_down')
media = Image('MediaButton.png', 24, 112, True, 'to_media')
button = Image('LargeButton.png', 24, 204, True, 'quit')
button2 = Image('LargeButton.png', 24, 296)
button3 = Image('LargeButton.png', 24, 296, True, 'to_start')
play = Image('Play.png', 58, 423, True, 'play_song')
pause = Image('Pause.png', 102, 423, True, 'stop_song')
stop = Image('Stop.png', 190, 423, True, 'stop_song')
skip_back = Image('Skip Back.png', 14, 423, True, 'previous_song')
skip_fwd = Image('Skip Forward.png', 146, 423, True, 'next_song')
song_scroller = ScrollingList(songlist, 500, 100, 200, 200, 3)

info_bar = Text('Words of Others', 246, 400, 'DS-DIGI.TTF', 52, (255,184,0))
info_bar.rect.right = 668
digital_clock = Text((strftime('%I')+':'+strftime('%M')), 680, 411, 'DS-DIGI.TTF', 60, (255,184,0))

always_up = [background, vol_up, vol_down, skip_back, skip_fwd, play, pause, stop, digital_clock, info_bar]
start = [media, button, button2]
media = [button, button3]
current = always_up

mousex = 0
mousey = 0
mouseclicked = False

while True:

	now = datetime.now()
	if now.hour > 12:
		chour = str(now.hour-12)
	elif now.hour == 0:
		chour = '12'
	else:
		chour = str(now.hour)
	digital_clock.text = chour + ':' + strftime('%M')
	for obj in current:
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
		for obj in current:
			if obj.clickable and obj.checkclick(mousex, mousey):
				action = obj.action
				if action == 'play_song':
					if music_paused:
						pygame.mixer.music.unpause()
						music_paused = False
					else:
						pygame.mixer.music.stop()
						pygame.mixer.music.load(songlist[current_song])
						pygame.mixer.music.set_volume(volume/30.0)
						pygame.mixer.music.play()
				elif action == 'stop_song':
					pygame.mixer.music.stop()
				elif action == 'next_song':
					pygame.mixer.music.stop()
					current_song += 1
					if current_song == len(songlist):
						current_song = 0
					pygame.mixer.music.load(songlist[current_song])
					pygame.mixer.music.set_volume(volume/30.0)
					pygame.mixer.music.play()
				elif action == 'previous_song':
					pygame.mixer.music.stop()
					if current_song == 0:
						current_song = len(songlist)						
					current_song -= 1
					pygame.mixer.music.load(songlist[current_song])
					pygame.mixer.music.set_volume(volume/30.0)
					pygame.mixer.music.play()
				elif action == 'pause_song':
					pygame.mixer.music.pause()
					music_paused = True
				elif action == 'volume_up':
					if volume < 30.0:
						volume += 1.0
						pygame.mixer.music.set_volume(volume/30.0)
				elif action == 'volume_down':
					if volume > 0.0:
						volume -= 1.0
						pygame.mixer.music.set_volume(volume/30.0)
				
	mouseclicked == False
	pygame.display.update()
	fpsClock.tick(FPS)
