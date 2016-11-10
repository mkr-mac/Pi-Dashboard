import pygame, os
from pygame.locals import *

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
		DS.blit(self.render, (self.x,self.y))
		
	def set_coords(self, xy):
		self.coords = xy
	
	def checkclick(self, mousex, mousey):
		return (self.y+self.height > mousey > self.y and 
				self.x+self.width > mousex > self.x)
	
	def set_text(self, new_str):
		self.text = new_str
		self.render = self.font.render(self.text, True, self.color)
		self.rect = self.render.get_rect()
		self.height = self.rect.height
		self.width = self.rect.width