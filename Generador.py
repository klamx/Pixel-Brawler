import pygame
import random

class Generador(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([60, 54])
		self.image.fill([0, 255, 0])
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		self.temp = random.randrange(100)
		self.f_velx = 0

	def update(self):
		self.temp -= 1
		self.rect.x += self.f_velx