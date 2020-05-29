import pygame
import random
from Jugador import Jugador
from Goblin import Goblin
#<<<<<<< HEAD
from Arrow import Arrow
#=======
from Generador import Generador
#>>>>>>> config_vidas

ANCHO = 500
ALTO = 340
NEGRO=[0,0,0]
VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
AMARILLO=[255,255,0]
BLANCO=[255,255,255]

def barra_vida(ventana, punto_a, punto_b, resta = 0, suma = 0):
	pygame.draw.line(ventana, ROJO, punto_a, [punto_b[0], punto_b[1]], 7)


if __name__ == '__main__':
	ventana = pygame.display.set_mode([ANCHO, ALTO])
	presentacion = False
	fin = False
	reloj = pygame.time.Clock()
	numero_goblins = 6

	# Seccion de presentacion
	bg_inicio = pygame.image.load('Backgrounds/inicio.png')
	arrow = pygame.image.load('Sprites/arrow.png')
	
	flechas = pygame.sprite.Group()
	flecha = Arrow([50, 195], arrow)
	flechas.add(flecha)

	while (not fin) and (not presentacion):
		# Gestion de eventos
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:
				#presentacion = True
				#print presentacion
				if event.key == pygame.K_DOWN:
					flecha.rect.y = 240

				if event.key == pygame.K_UP:
					flecha.rect.y = 195

				if flecha.rect.y == 195 and event.key == pygame.K_RETURN:
					presentacion = True
					flechas.remove(flecha)

				if flecha.rect.y == 240 and event.key == pygame.K_RETURN:
					presentacion = True
					fin = True


		ventana.fill(NEGRO)
		ventana.blit(bg_inicio, [0, 0])
		flechas.update()
		flechas.draw(ventana)
		pygame.display.flip()


	# Seccion de configuracion del nivel
	# Grupos
	jugadores = pygame.sprite.Group()
	goblins = pygame.sprite.Group()
	generadores = pygame.sprite.Group()

	# Imagenes
	# Backgrounds
	background1 = pygame.image.load('Backgrounds/Battleground2a.png')
	background1_info = background1.get_rect()
	background1_velx = 0
	background1_posx = 0
	limite_derecho = 350
	background1_limite_derecho = ANCHO - background1_info[2]

	# Jugador
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

	# Goblin
	goblin_right = pygame.image.load('Sprites/Goblin/goblin.centurion.png')
	goblin_left = pygame.image.load('Sprites/Goblin/goblin.centurion_left.png')

	# Corazones
	corazon1 = pygame.image.load('Sprites/Heart/heart_16x16.png')
	corazon1gray = pygame.image.load('Sprites/Heart/heart_16x16_gray.png')
	corazonx32 = pygame.image.load('Sprites/Heart/heart_32x32.png')

	# Sprites jugador
	m = []
	# accion 0 idle
	for j in range(1):
		fila = []
		for c in range(4):
			cuadro = man_idle.subsurface(96 * c, 96 * j, 96, 96)
			fila.append(cuadro)
		m.append(fila)

	# accion 1 death
	for j in range(1):
		fila = []
		for c in range(4):
			cuadro = man_death.subsurface(96 * c, 96 * j, 96, 96)
			fila.append(cuadro)
		m.append(fila)

	# accion 2 attack right
	for j in range(1):
		fila = []
		for c in range(4):
			cuadro = man_attack.subsurface(96 * c, 96 * j, 96, 96)
			fila.append(cuadro)
		m.append(fila)

	# accion 3 walk right
	for j in range(1):
		fila = []
		for c in range(6):
			cuadro = man_walk.subsurface(96 * c, 96 * j, 96, 96)
			fila.append(cuadro)
		m.append(fila)

	# accion 4 hurt
	for j in range(1):
		fila = []
		for c in range(2):
			cuadro = man_hurt.subsurface(96 * c, 96 * j, 96, 96)
			fila.append(cuadro)
		m.append(fila)

	# accion 5 idle left
	for j in range(1):
		fila = []
		for c in range(4):
			cuadro = man_idle_left.subsurface(96 * c, 96 * j, 96, 96)
			fila.append(cuadro)
		m.append(fila)

	# accion 6 death left
	for j in range(1):
		fila = []
		for c in range(4):
			cuadro = man_death_left.subsurface(96 * c, 96 * j, 96, 96)
			fila.append(cuadro)
		m.append(fila)

	# accion 7 attack left
	for j in range(1):
		fila = []
		for c in range(4):
			cuadro = man_attack_letf.subsurface(96 * c, 96 * j, 96, 96)
			fila.append(cuadro)
		m.append(fila)

	# accion 8 walk left
	for j in range(1):
		fila = []
		for c in range(6):
			cuadro = man_walk_left.subsurface(96 * c, 96 * j, 96, 96)
			fila.append(cuadro)
		m.append(fila)

	# accion 9 hurt left
	for j in range(1):
		fila = []
		for c in range(2):
			cuadro = man_hurt_left.subsurface(96 * c, 96 * j, 96, 96)
			fila.append(cuadro)
		m.append(fila)

	# Sprites goblin
	matriz_goblin = []
	#for j in range(4):
	#	fila = []
	#	for c in range(10):
	#		cuadro = goblin_right.subsurface(64 * c, 128 * j, 64, 128)
	#		fila.append(cuadro)
	#	matriz_goblin.append(fila)

	for j in range(4):
		fila = []
		for c in range(10):
			cuadro = goblin_left.subsurface(64 * c, 128 * j, 64, 128)
			fila.append(cuadro)
		matriz_goblin.append(fila)

	jugador = Jugador([50, 240], m)
	jugadores.add(jugador)

	#goblin = Goblin([490, 210], matriz_goblin)
	#goblins.add(goblin)

	#generador1 = Generador([420, 184])
	generador1 = Generador([620, 184])
	generadores.add(generador1)


	# fuente = pygame.font.Font(None, 40)
	# mensaje = fuente.render('Juego', True, BLANCO)
	# posicion final de la barra de vida
	posf_x = 110
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
					#jugador.rect.x = jugador.rect.x - 48

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
		# Desplazamiento fondo
		if jugador.rect.x > limite_derecho:
			jugador.rect.x = limite_derecho

			if background1_posx > background1_limite_derecho:
				background1_velx = -5

			else:
				background1_velx = 0

		else:
			background1_velx = 0

		if jugador.rect.x < -20:
			jugador.rect.x = -20


		# Control Generadores
		for g in generadores:
			if g.temp < 0 and numero_goblins > 0:
				centro = list(g.rect.center)
				goblin = Goblin([centro[0], centro[1]], matriz_goblin)
				numero_goblins -= 1
				g.temp = 30
				print centro[0], centro[1]
				goblins.add(goblin)

			g.f_velx = background1_velx

		# Barra
		#posf_x = 110

		# Control Goblins
		for g in goblins:
			if pygame.sprite.collide_circle(jugador, g):
				g.accion = 2
				g.velx = 0
				if jugador.vidas >= 0:
					if jugador.salud > 0:
						jugador.salud -= g.damage
						posf_x -= g.damage
						print jugador.salud, posf_x
					else:
						jugador.vidas -= 1
						jugador.salud = 100
						posf_x = 110

				if jugador.accion == 2 or jugador.accion == 7:
					if g.salud >= 0:
						g.salud -= jugador.damage
					else:
						goblins.remove(g)

			else:
				g.accion = 0
				g.velx = -5


		if jugador.vidas == 0:
			fin_juego = True
		# Control vidas

		


		# Refresco
		jugadores.update()
		generadores.update()
		goblins.update()
		generadores.draw(ventana)
		ventana.blit(background1, [background1_posx, 0])
		barra_vida(ventana, [10, 20], [posf_x, 20])
		if jugador.vidas == 3:
			ventana.blit(corazon1, [130, 15])
			ventana.blit(corazon1, [150, 15])
			ventana.blit(corazon1, [170, 15])
		elif jugador.vidas == 2:
			ventana.blit(corazon1, [130, 15])
			ventana.blit(corazon1, [150, 15])
			ventana.blit(corazon1gray, [170, 15])
		elif jugador.vidas == 1:
			ventana.blit(corazon1, [130, 15])
			ventana.blit(corazon1gray, [150, 15])
			ventana.blit(corazon1gray, [170, 15])
		elif jugador.vidas == 0:
			ventana.blit(corazon1gray, [130, 15])
			ventana.blit(corazon1gray, [150, 15])
			ventana.blit(corazon1gray, [170, 15])
		#barra_vida.draw(ventana)
		
		jugadores.draw(ventana)
		goblins.draw(ventana)
		pygame.display.flip()
		reloj.tick(12)
		background1_posx += background1_velx

	# Fin de juego
	#fuente = pygame.font.Font(None, 40)
	#mensaje = fuente.render('Fin de juego', True, BLANCO)

	game_over = pygame.image.load('Backgrounds/GameOver.png')

	while not fin:
		# Gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:
				fin = True

		ventana.fill(NEGRO)
		ventana.blit(game_over, [0, 0])
		pygame.display.flip()