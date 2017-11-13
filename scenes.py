import sys, pygame, random, os
from image import Image
from text import Text
from music_utils import *
from scrolling_list import ScrollingList

#Background image
background = Image('Background.png', 0, 0)
#Music controls
play = Image('Play.png', 58, 423, True, 'play_song')
pause = Image('Pause.png', 102, 423, True, 'pause_song')
stop = Image('Stop.png', 190, 423, True, 'stop_song')
skip_back = Image('Skip Back.png', 14, 423, True, 'previous_song')
skip_fwd = Image('Skip Forward.png', 146, 423, True, 'next_song')

#Volume display and controls
vol_bar_green = pygame.image.load(os.path.join("Images",'Volume Bar Green.png'))
vol_bar_yellow = pygame.image.load(os.path.join("Images",'Volume Bar Yellow.png'))
vol_bar_red = pygame.image.load(os.path.join("Images",'Volume Bar Red.png'))
vol_up = Image('Volume Up.png', 15, 7, True, 'volume_up')
vol_down = Image('Volume Down.png', 15, 364, True, 'volume_down')

#misc
tracker = Image('Tab.png', 346, 448)
tracker_sensor = Image('Tracker Sensor.png', 353, 447, True, 'to_song_position')
songlist = getsonglist()
song_scroller = ScrollingList(songlist, 400, 0, 200, 200, 10)
apic = Image('album.jpg', 200, 200)

#Right-side buttons
media_button = Image('Media.png', 700, 0, True, 'to_media')
navigation_button = Image('Navigation.png', 700, 80, True, 'to_navigation')
games_button = Image('Games.png', 700, 160, True, 'to_games')
diagnostics_button = Image('Diagnostics.png', 700, 240, True, 'to_diagnostics')
settings_button = Image('Settings.png', 700, 320, True, 'to_settings')

#The text displays that always show
info_bar = Text(songlist[0].infolayout, 242, 400, os.path.join("Fonts",'DS-DIGI.TTF'), 52, (255,184,0), 426, True)
digital_clock = Text('18:88', 662, 411, os.path.join("Fonts",'DS-DIGI.TTF'), 60, (255,184,0))
song_time = Text('0:00', 292, 451, os.path.join("Fonts",'DS-DIGI.TTF'), 28, (255,184,0))

##The various lists of objects that make up the screens that can be loaded
#These can be added together to easily combine screens/reduce redundancy
#example: current = always_up + media
always_up = [background, vol_up, vol_down, skip_back, skip_fwd, 
        play, pause, stop, digital_clock, info_bar, song_time, 
        tracker, tracker_sensor, media_button, navigation_button,
        games_button, diagnostics_button, settings_button]

media = [song_scroller, apic]
