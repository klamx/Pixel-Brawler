import pygame

class Goblin(pygame.sprite.Sprite):
	def __init__(self, posicion, m):
		pygame.sprite.Sprite.__init__(self)
		self.m = m
		self.con = 0
		self.accion = 0
		self.image = self.m[self.accion][0]
		self.rect = self.image.get_rect()
		self.rect.x = posicion[0]
		self.rect.y = posicion[1]
		self.velx = 0

	def update(self):
		self.rect.x += self.velx

		if self.con < 6:
			self.con += 1
		else:
			self.con = 0

		self.image = self.m[self.accion][self.con]