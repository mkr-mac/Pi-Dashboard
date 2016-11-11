import pygame, os
from pygame.locals import *

class Image:
	def __init__(self, image, x, y, clickable = False, action = None):
		self.x = x
		self.y = y
		self.coords = (x,y)
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.clickable = clickable
		self.action = action
	
	def draw(self, DS):
		DS.blit(self.image, (self.x,self.y))
	
	def checkclick(self, mousex, mousey):
		return (self.y+self.height > mousey > self.y and 
				self.x+self.width > mousex > self.x)
				
	def change_pic(image):
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.width = self.image.get_width()
		self.height = self.image.get_height()
