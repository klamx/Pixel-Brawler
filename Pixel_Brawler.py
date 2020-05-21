import pygame
from Jugador import Jugador
ANCHO = 500
ALTO = 400
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
	jugadores = pygame.sprite.Group()

	# Imagenes
	man_idle = pygame.image.load('Sprites/Man/Man_idle.png')
	man_death = pygame.image.load('Sprites/Man/Man_death.png')
	man_hurt = pygame.image.load('Sprites/Man/Man_hurt.png')
	man_walk = pygame.image.load('Sprites/Man/Man_walk.png')
	man_attack = pygame.image.load('Sprites/Man/Man_attack.png')
	man_idle_left = pygame.image.load('Sprites/Man/Man_idle_left.png')
	man_death_left = pygame.image.load('Sprites/Man/Man_death_left.png')
	man_hurt_left = pygame.image.load('Sprites/Man/Man_hurt_left.png')
	man_walk_left = pygame.image.load('Sprites/Man/Man_walk_left.png')
	man_attack_letf = pygame.image.load('Sprites/Man/Man_attack_left.png')

	m = []
	# accion 0 idle
	for j in range(1):
		fila = []
		for c in range(4):
			cuadro = man_idle.subsurface(48 * c, 48 * j, 48, 48)
			fila.append(cuadro)
		m.append(fila)

	# accion 1 death
	for j in range(1):
		fila = []
		for c in range(4):
			cuadro = man_death.subsurface(48 * c, 48 * j, 48, 48)
			fila.append(cuadro)
		m.append(fila)

	# accion 2 attack right
	for j in range(1):
		fila = []
		for c in range(4):
			cuadro = man_attack.subsurface(48 * c, 48 * j, 48, 48)
			fila.append(cuadro)
		m.append(fila)

	# accion 3 walk left
	for j in range(1):
		fila = []
		for c in range(6):
			cuadro = man_walk.subsurface(48 * c, 48 * j, 48, 48)
			fila.append(cuadro)
		m.append(fila)

	# accion 4 hurt
	for j in range(1):
		fila = []
		for c in range(2):
			cuadro = man_hurt.subsurface(48 * c, 48 * j, 48, 48)
			fila.append(cuadro)
		m.append(fila)

	# accion 5 idle left
	for j in range(1):
		fila = []
		for c in range(4):
			cuadro = man_idle_left.subsurface(48 * c, 48 * j, 48, 48)
			fila.append(cuadro)
		m.append(fila)

	# accion 6 death left
	for j in range(1):
		fila = []
		for c in range(4):
			cuadro = man_death_left.subsurface(48 * c, 48 * j, 48, 48)
			fila.append(cuadro)
		m.append(fila)

	# accion 7 attack left
	for j in range(1):
		fila = []
		for c in range(4):
			cuadro = man_attack_letf.subsurface(48 * c, 48 * j, 48, 48)
			fila.append(cuadro)
		m.append(fila)

	# accion 8 walk left
	for j in range(1):
		fila = []
		for c in range(6):
			cuadro = man_walk_left.subsurface(48 * c, 48 * j, 48, 48)
			fila.append(cuadro)
		m.append(fila)

	# accion 9 hurt left
	for j in range(1):
		fila = []
		for c in range(2):
			cuadro = man_hurt_left.subsurface(48 * c, 48 * j, 48, 48)
			fila.append(cuadro)
		m.append(fila)

	jugador = Jugador([100, 100], m)
	jugadores.add(jugador)

	# fuente = pygame.font.Font(None, 40)
	# mensaje = fuente.render('Juego', True, BLANCO)
	fin_juego = False
	# Seccion de eventos
	while (not fin) and (not fin_juego):
		# Gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:
				# Caminar hacia la derecha
				if event.key == pygame.K_RIGHT:
					jugador.dir = 1
					jugador.accion = 3
					jugador.velx = 5

				# Caminar hacia la izquierda
				if event.key == pygame.K_LEFT:
					jugador.dir = 0
					jugador.accion = 8
					jugador.velx = -5

				# Golpear 
				if event.key == pygame.K_c:
					# Mirando hacia la derecha
					if jugador.dir == 1:
						jugador.accion = 2
					# Mirando hacia la izquierda
					else:
						jugador.accion = 7


			if event.type == pygame.KEYUP:

				if jugador.dir == 1:
					jugador.accion = 0
					jugador.velx = 0

				else:
					jugador.accion = 5
					jugador.velx = 0

		# Control

		# Refresco
		jugadores.update()
		ventana.fill(NEGRO)
		jugadores.draw(ventana)
		pygame.display.flip()
		reloj.tick(13)

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