import pygame

class BarraVida(pygame.sprite.Sprite):
	def __init__(self, posicion, dim_an, dim_al):
		pygame.sprite.Sprite.__init__(self)
		self.dim_an = dim_an
		self.image = pygame.Surface([self.dim_an, dim_al])
		self.image.fill([255, 0, 0])
		self.rect = self.image.get_rect()
		self.rect.x = posicion[0]
		self.rect.y = posicion[1]

	def update(self):
		self.dim_an = self.dim_an