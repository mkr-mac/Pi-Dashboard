import sys, pygame, random, os
from time import strftime, gmtime
from sound import Sound
from image import Image
from text import Text
from scrolling_list import ScrollingList
from pygame.locals import *
from music_utils import *
from utils import *

def quit():
  pygame.quit()
  sys.exit()

#Screen size constants
SCREENWIDTH = 800
SCREENHEIGHT = 480
FULLSCREEN = False

#Start Pygame
pygame.init()
FPS = 60.0
fpsClock  = pygame.time.Clock()
if FULLSCREEN:
  DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
else:
  DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption('Pi-Board')

#Initial volume 30.0 max
volume = 30.0
music_paused = False

#Load in scenes
from scenes import *
current_song = 0

#All items in this list will be drawn
current_scene = always_up

#Initial mouse position
#to be used in a possible improvement to touch click accuracy
mousex = 0
mousey = 0
mouseclicked = False
tracker_time = 0.0
music_pos = 0

"""The main loop"""
while True:

  digital_clock.set_text(get_clock_time())

  music_playing = pygame.mixer.music.get_busy()
  old_time = music_pos
  music_pos = pygame.mixer.music.get_pos()
  if music_playing and music_pos > 0 and ((music_pos - old_time) > 0):
    delta = (music_pos - old_time)/1000.0
    tracker_time += delta
  if not music_playing and not music_paused:
    tracker_time = 0
  tracker.x = 346 + 300*(tracker_time/(songlist[current_song].length))

  if tracker_time < 0:
    song_time.set_text("0:00")
  elif tracker_time%60<10:
    song_time.set_text(str(int(tracker_time/60))+":0"+str(int(tracker_time%60)))
  else:
    song_time.set_text(str(int(tracker_time/60))+":"+str(int(tracker_time%60)))
  
  # Draw all the objects in the current layout
  for obj in current_scene:
    obj.draw(DS)
  
  # Drawing the volume bars
  if volume>0:
    for n in range(int(volume)):
      if n<10:
        DS.blit(vol_bar_green, (15,(-10*n)+346))
      elif n<20:
        DS.blit(vol_bar_yellow, (15,(-10*n)+346))
      else:
        DS.blit(vol_bar_red, (15,(-10*n)+346))
  
  # Checking for mouse/touch events
  for event in pygame.event.get():
    if event.type == QUIT:
      quit()
    if event.type == MOUSEMOTION:
      mousex, mousey = event.pos
    if event.type == MOUSEBUTTONDOWN:
      mouseclicked = True
    if event.type == MOUSEBUTTONUP:
      mouseclicked = False
  
  # Actions on click
  if mouseclicked == True:
    for obj in current_scene:
      if obj.clickable and obj.checkclick(mousex, mousey):
        action = obj.action
        if action == 'play_song':
          pygame.mixer.music.unpause()
          if not music_playing:
            tracker_time = 0
            music_paused = False
            play_action(songlist[current_song].sound, volume, music_paused, music_playing)
        elif action == 'stop_song':
          tracker_time = 0
          stop_song()
        elif action == 'next_song':
          tracker_time = 0
          current_song = next_song(songlist, current_song, volume, music_playing)
          info_bar.set_text(songlist[current_song].infolayout)
        elif action == 'previous_song':
          tracker_time = 0
          current_song = prev_song(songlist, current_song, tracker_time, volume, music_playing)
          info_bar.set_text(songlist[current_song].infolayout)
        elif action == 'pause_song':
          music_paused = pause_song(music_playing)
        elif action == 'volume_up':
          volume = volume_up(volume)
        elif action == 'volume_down':
          volume = volume_down(volume)
        elif action == 'to_song_position':
          if songlist[current_song].sound.endswith(".mp3") or songlist[current_song].sound.endswith(".ogg"):
            music_paused = False
            play_action(songlist[current_song].sound, volume, music_paused, False)
            pygame.mixer.music.rewind()
            time_spot = ((float(mousex)-353.0)/300.0)*(songlist[current_song].length)
            tracker_time = time_spot
            pygame.mixer.music.set_pos(time_spot)
        elif action == 'to_media':
          current_scene += media
        elif action[0:16] == 'set_current_song':
          print('Hey')
          tracker_time = 0
          current_song = next_song(songlist, int(action[-7:])-1, volume, music_playing)
          info_bar.set_text(songlist[current_song].infolayout)
          if songlist[current_song].album_art:
            with open('album.jpg', 'w') as img:
              img.write(songlist[current_song].album_art)
          apic.change_pic('album.jpg')

        else:
          print("Unsupported action: " + action)
              
  mouseclicked = False
  pygame.display.update()
  fpsClock.tick(FPS)
