import pygame

class Jugador(pygame.sprite.Sprite):
	def __init__(self, posicion, m):
		pygame.sprite.Sprite.__init__(self)
		self.radius = 10
		self.m = m
		self.dir = 1
		self.con = 0
		self.accion = 0
		self.image = self.m[self.accion][0]
		self.rect = self.image.get_rect()
		self.rect.x = posicion[0]
		self.rect.y = posicion[1]
		self.velx = 0
		self.vely = 0
		self.salud = 100
		self.vidas = 2
		self.damage = 20

		if self.accion == 0 or self.accion == 1 or self.accion == 2 or self.accion == 5 or self.accion == 6 or self.accion == 7:
			self.limite = 3
		elif self.accion == 3 or self.accion == 8:
			self.limite = 5
		elif self.accion == 4 or self.accion == 9:
			self.limite = 1


	def update(self):
		self.rect.x += self.velx
		self.rect.y += self.vely
		
		#if self.dir == 0:
		#	self.accion = 5
		#else:
		#	self.accion = 0


		if self.con < self.limite:
			self.con += 1
		else:
			self.con = 0

		self.image = self.m[self.accion][self.con]


	def RetPos(self):
		x = self.rect.x
		y = self.rect.y
		return [x, y]
