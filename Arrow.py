import pygame

class Arrow(pygame.sprite.Sprite):
	def __init__(self, posicion, m):
		pygame.sprite.Sprite.__init__(self)
		self.image = m;
		self.rect = self.image.get_rect()
		self.rect.x = posicion[0]
		self.rect.y = posicion[1]

	def update(self):
		self.rect.x = self.rect.x
		self.rect.y = self.rect.y
