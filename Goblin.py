import pygame

class Goblin(pygame.sprite.Sprite):
	def __init__(self, posicion, m):
		pygame.sprite.Sprite.__init__(self)
		self.radius = 8
		self.m = m
		self.con = 9
		self.accion = 0
		self.image = self.m[self.accion][0]
		self.rect = self.image.get_rect()
		self.rect.x = posicion[0]
		self.rect.y = posicion[1]
		self.velx = 0
		self.salud = 100
		self.damage = 10

	def update(self):
		self.rect.x += self.velx

		if self.con > 5:
			self.con -= 1
		else:
			self.con = 9

		self.image = self.m[self.accion][self.con]