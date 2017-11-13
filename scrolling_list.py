import pygame, os
from text import Text
from pygame.locals import *

#Broken
class ScrollingList:
  def __init__(self, string_list, x, y, width, height, blocks_to_display):
    self.string_list = string_list
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
    
    for stri in self.string_list:
      stri = Text(stri.infolayout, 0, 0, 'freesansbold.ttf',32 , (255,255,255), None, False, True, 'set_current_song' + str(len(self.text_boxes)).zfill(7))
      stri.width = self.width
      stri.height = self.height
      self.text_boxes.append(stri)
    
  def draw(self, DS):
    for num in range(self.blocks_to_display):
      if num >= len(self.text_boxes):
        self.text_boxes[num +- len(text_boxes) + self.current_block].set_coords((self.x, self.y+num*self.block_height))
      else:
        self.text_boxes[num + self.current_block].set_coords((self.x, self.y+(num*self.block_height)))

      self.text_boxes[self.current_block+num].draw(DS)
  
  def checkclick(self, mousex, mousey):
    for block in range(self.current_block, self.current_block + self.blocks_to_display):
      gl_num = self.current_block + block
      if (self.y+(block+1)*self.block_height > mousey > self.y and self.x+self.width > mousex > self.x):
        self.action = self.text_boxes[self.current_block+block].action
        return True
    return False
