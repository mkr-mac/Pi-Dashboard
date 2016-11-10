import sys, pygame, random, os
from sound import Sound
from image import Image
from text import Text
from scrolling_list import ScrollingList
from pygame.locals import *
from time import strftime, gmtime
from datetime import datetime

def quit():
	pygame.quit()
	sys.exit()

def play_song():
	pygame.mixer.music.stop()
	pygame.mixer.music.load(songlist[current_song])
	pygame.mixer.music.play()

def set_current_song(song):
	current_song = song
	return ''
	
def stop_song():
	pygame.mixer.music.stop()

"""UNUSED
def rot_center(image, angle):
	#rotate an image while keeping its center and size
	orig_rect = image.get_rect()
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = orig_rect.copy()
	rot_rect.center = rot_image.get_rect().center
	rot_image = rot_image.subsurface(rot_rect).copy()
	return rot_image
"""

def getsonglist():
	songs = []
	for root, dirs, files in os.walk(os.getcwd()):
		for file in files:
			end = file.endswith
			if end(".mp3") or end(".wav") or end(".flac") or end(".ogg"):
				songs.append(Sound(os.path.join(root, file)))
	return songs
	#TODO: organize/sort songs
	#return sorted(songs, key=str.lower)

#Screen size constants
SCREENWIDTH = 800
SCREENHEIGHT = 480
FULLSCREEN = False

#Start Pygame
pygame.init()
FPS = 60
fpsClock  = pygame.time.Clock()
if FULLSCREEN:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
else:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption('Pi-Board')

#get the music stored locally
songlist = getsonglist()
current_song = 0
#Initial volume 30.0 max
volume = 30.0
music_paused = False

"""Loading in the images"""
#Background image
background = Image('Background.png', 0, 0)
#Music controls
play = Image('Play.png', 58, 423, True, 'play_song')
pause = Image('Pause.png', 102, 423, True, 'pause_song')
stop = Image('Stop.png', 190, 423, True, 'stop_song')
skip_back = Image('Skip Back.png', 14, 423, True, 'previous_song')
skip_fwd = Image('Skip Forward.png', 146, 423, True, 'next_song')

#Volume display and controls
vol_bar_green = pygame.image.load('Volume Bar Green.png')
vol_bar_yellow = pygame.image.load('Volume Bar Yellow.png')
vol_bar_red = pygame.image.load('Volume Bar Red.png')
vol_up = Image('Volume Up.png', 15, 7, True, 'volume_up')
vol_down = Image('Volume Down.png', 15, 364, True, 'volume_down')

#misc
media = Image('MediaButton.png', 24, 112, True, 'to_media')
button = Image('LargeButton.png', 24, 204, True, 'quit')
button2 = Image('LargeButton.png', 24, 296)
button3 = Image('LargeButton.png', 24, 296, True, 'to_start')
song_scroller = ScrollingList(songlist, 500, 100, 200, 200, 3)

#The text displays that always show
info_bar = Text(songlist[current_song].infolayout, 246, 400, 'DS-DIGI.TTF', 52, (255,184,0))
info_bar.x = 668 - info_bar.width
digital_clock = Text((strftime('%I')+':'+strftime('%M')), 680, 411, 'DS-DIGI.TTF', 60, (255,184,0))
song_time = Text('0:00', 242, 453, 'DS-DIGI.TTF', 28, (255,184,0))

#The various lists of objects that make up the screens that can be loaded
#These can be added together to easily combine screens/reduce redundancy
#example: current = always_up + media
always_up = [background, vol_up, vol_down, skip_back, skip_fwd, 
				play, pause, stop, digital_clock, info_bar, song_time]
start = [media, button, button2]
media = [button, button3]
#All items in this list will be drawn
current = always_up

#Initial mouse position
#to be used in a possible improvement to touch click accuracy
mousex = 0
mousey = 0
mouseclicked = False

"""The main loop"""
while True:
	now = datetime.now()
	if now.hour > 12:
		chour = str(now.hour-12)
	elif now.hour == 0:
		chour = '12'
	else:
		chour = str(now.hour)
	digital_clock.set_text(chour + ':' + strftime('%M'))
	digital_clock.x = 794 - digital_clock.width
	tracker_time = pygame.mixer.music.get_pos()
	song_time.text = str(tracker_time/1000)
	
	for obj in current:
		obj.draw(DS)
	
	#Drawing the volume bars
	if volume>0:
		for n in range(int(volume)):
			if n<10:
				DS.blit(vol_bar_green, (15,(-10*n)+346))
			elif n<20:
				DS.blit(vol_bar_yellow, (15,(-10*n)+346))
			else:
				DS.blit(vol_bar_red, (15,(-10*n)+346))
	
	for event in pygame.event.get():
		if event.type == QUIT:
			quit()
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
		elif event.type == MOUSEBUTTONDOWN:
			mouseclicked = True
		elif event.type == MOUSEBUTTONUP:
			mouseclicked = False
	
	#Actions on click
	#Really needs cleaned up
	if mouseclicked == True:
		for obj in current:
			if obj.clickable and obj.checkclick(mousex, mousey):
				action = obj.action
				#Change things to function calls
				if action == 'play_song':
					if music_paused:
						pygame.mixer.music.unpause()
						music_paused = False
					else:
						pygame.mixer.music.stop()
						pygame.mixer.music.load(songlist[current_song].sound)
						pygame.mixer.music.set_volume(volume/30.0)
						pygame.mixer.music.play()
				elif action == 'stop_song':
					pygame.mixer.music.stop()
				elif action == 'next_song':
					pygame.mixer.music.stop()
					current_song += 1
					if current_song == len(songlist):
						current_song = 0
					info_bar.set_text(songlist[current_song].infolayout)
					info_bar.x = 668 - info_bar.width
					pygame.mixer.music.load(songlist[current_song].sound)
					pygame.mixer.music.set_volume(volume/30.0)
					pygame.mixer.music.play()
				elif action == 'previous_song':
					pygame.mixer.music.stop()
					if current_song == 0:
						current_song = len(songlist)						
					current_song -= 1
					info_bar.set_text(songlist[current_song].infolayout)
					info_bar.x = 668 - info_bar.width
					pygame.mixer.music.load(songlist[current_song].sound)
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
				
	mouseclicked = False
	pygame.display.update()
	fpsClock.tick(FPS)
