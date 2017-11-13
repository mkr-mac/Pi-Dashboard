import sys, pygame, random, os
from sound import Sound

def play_action(song, volume, paused, playing):
  pygame.mixer.music.unpause()
  pygame.mixer.music.stop()
  pygame.mixer.music.load(song)
  pygame.mixer.music.set_volume(volume/30.0)
  pygame.mixer.music.play()

def next_song(songlist, current_song, volume, playing):
  stop_song()
  current_song += 1
  if current_song == len(songlist):
    current_song = 0
  #info_bar.x = 668 - info_bar.width
  play_action(songlist[current_song].sound, volume, False, not playing)
  return current_song

def set_song(songlist, current_song, volume, playing):
  stop_song()
  current_song += 1
  if current_song == len(songlist):
    current_song = 0
  #info_bar.x = 668 - info_bar.width
  play_action(songlist[current_song].sound, volume, False, not playing)
  return current_song
  
def prev_song(songlist, current_song, tracker_time, volume, playing):
  if tracker_time > 3 and playing:
    play_action(songlist[current_song].sound, volume, False, False)
  else:
    stop_song()
    if current_song == 0:
      current_song = len(songlist)            
    current_song -= 1
    #info_bar.x = 668 - info_bar.width
    play_action(songlist[current_song].sound, volume, False, not playing)
  return current_song
  
def pause_song(playing):
  if playing:
    pygame.mixer.music.pause()
    return True
  return False

def stop_song():
  pygame.mixer.music.stop()

def getsonglist():
  songs = []
  for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
      end = file.endswith
      if end(".mp3") or end(".wav") or end(".flac") or end(".ogg"):
        songs.append(Sound(os.path.join(root, file)))
  songs.sort(key=lambda x: x.title.lower())
  return songs