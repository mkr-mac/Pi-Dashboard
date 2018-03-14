import sys, pygame, random, os
from image import DashImage
from PIL import Image
from time import strftime, gmtime, time
from datetime import datetime

def volume_up(volume):
  if volume < 30.0:
    volume += 1.0
    pygame.mixer.music.set_volume(volume/30.0)
  return volume

def volume_down(volume):
  if volume > 0.0:
    volume -= 1.0
    pygame.mixer.music.set_volume(volume/30.0)
  return volume

"""UNUSED`
def rot_center(image, angle):
  #rotate an image while keeping its center and size
  orig_rect = image.get_rect()
  rot_image = pygame.transform.rotate(image, angle)
  rot_rect = orig_rect.copy()
  rot_rect.center = rot_image.get_rect().center
  rot_image = rot_image.subsurface(rot_rect).copy()
  return rot_image
"""

def get_clock_time():
  #Update the clock
  now = datetime.now()
  if now.hour > 12:
    chour = str(now.hour-12)
  elif now.hour == 0:
    chour = '12'
  else:
    chour = str(now.hour)
  if int(chour) < 10:
    chour = ' ' + chour

  return(chour + ':' + strftime('%M'))

def resize_image(dashimage, size_x, size_y):
  img = Image.open(dashimage.url)
  result_img = img.resize((size_x, size_y), Image.ANTIALIAS)
  result_img.save(os.path.join("Images", "temp.jpg"))
  img.close()
  dashimage.change_pic(os.path.join("Images", "temp.jpg"))
