import os, pygame
from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, ID3NoHeaderError, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC
from mutagen.easyid3 import EasyID3

class Sound:
	def __init__(self, sound):
		self.sound = sound
		if sound.endswith(".mp3"):
			self.length = MP3(sound).info.length
		else:
			self.length = pygame.mixer.Sound(sound).get_length()
		print self.length
		self.path, self.filename = os.path.split(sound)
		try: 
			self.soundID3 = ID3(sound)
		except ID3NoHeaderError:
			self.soundID3 = ID3()
		try:
			self.title = str(self.soundID3["TIT2"])
		except KeyError:
			self.title = str(self.filename)
		try:
			self.album = str(self.soundID3["TALB"])
		except KeyError:
			self.album = ''
		try:
			self.band = str(self.soundID3["TPE2"])
		except KeyError:
			self.band = ''
		try:
			self.description = str(self.soundID3["COMM"])
		except KeyError:
			self.description = ''
		try:
			self.artist = str(self.soundID3["TPE1"])
		except KeyError:
			self.artist = ''
		try:
			self.composer = str(self.soundID3["TCOM"])
		except KeyError:
			self.composer = ''
		try:
			self.genre = str(self.soundID3["TCON"])
		except KeyError:
			self.genre = ''
		try:
			self.year = str(self.soundID3["TDRC"])
		except KeyError:
			self.year = ''
		try:
			self.track_number = str(self.soundID3["TRCK"])
		except KeyError:
			self.track_number = ''
		self.infolayout = '    '+ self.title
		