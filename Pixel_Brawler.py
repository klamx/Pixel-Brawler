import pygame

ANCHO = 700
ALTO = 500
NEGRO=[0,0,0]
VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
AMARILLO=[255,255,0]
BLANCO=[255,255,255]

if __name__ == '__main__':
	ventana = pygame.display.set_mode([ANCHO, ALTO])
	presentacion = False
	fin = False
	reloj = pygame.time.Clock()


	# Seccion de presentacion
	pygame.font.init()
	fuente = pygame.font.Font(None, 40)
	mensaje = fuente.render('Inicio', True, BLANCO)

	while (not fin) and (not presentacion):
		# Gestion de eventos
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:
				presentacion = True
				print presentacion

		ventana.fill(NEGRO)
		ventana.blit(mensaje, [450, 350])
		pygame.display.flip()


	# Seccion de configuracion del nivel
	# Grupos


	fuente = pygame.font.Font(None, 40)
	mensaje = fuente.render('Juego', True, BLANCO)
	fin_juego = False
	# Seccion de eventos
	while (not fin) and (not fin_juego):
		# Gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:
				print 'asd'


		# Control

		# Refresco
		ventana.fill(NEGRO)
		ventana.blit(mensaje, [450, 200])
		pygame.display.flip()
		reloj.tick(15)

	# Fin de juego
	fuente = pygame.font.Font(None, 40)
	mensaje = fuente.render('Fin de juego', True, BLANCO)

	while not fin:
		# Gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

		ventana.fill(NEGRO)
		ventana.blit(mensaje, [450, 350])
		pygame.display.flip()