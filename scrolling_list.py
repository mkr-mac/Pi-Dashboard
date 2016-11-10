import pygame, os
from text import Text
from pygame.locals import *

#Broken
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
