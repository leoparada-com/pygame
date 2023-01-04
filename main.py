import pygame
# https://www.linkedin.com/in/leoparada/

# Inicializa Pygame
pygame.init()

# Establece el tamaño de la ventana
window_size = (400, 400)

# Crea la ventana
screen = pygame.display.set_mode(window_size)

# Establece el título de la ventana
pygame.display.set_caption("Mi juego")

# Establece la velocidad del cuadro
speed = 5

# Establece las dimensiones del cuadro
box_size = (50, 50)

# Establece la posición inicial del cuadro
box_pos = [100, 100]

# Crea el cuadro
box = pygame.Rect(box_pos, box_size)

# Establece el color del cuadro
box_color = (255, 0, 0)

# Ejecuta el juego
running = True
while running:
    # Obtiene todos los eventos del juego
    for event in pygame.event.get():
        # Si el evento es de tipo QUIT o la tecla X, cierra el juego
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False


    # Obtiene el estado de las teclas
    keys = pygame.key.get_pressed()

    # Si se presiona la flecha derecha, mueve el cuadro a la derecha
    if keys[pygame.K_RIGHT]:
        box.x += speed
    # Si se presiona la flecha izquierda, mueve el cuadro a la izquierda
    if keys[pygame.K_LEFT]:
        box.x -= speed
    # Si se presiona la flecha arriba, mueve el cuadro hacia arriba
    if keys[pygame.K_UP]:
        box.y -= speed
    # Si se presiona la flecha abajo, mueve el cuadro hacia abajo
    if keys[pygame.K_DOWN]:
        box.y += speed

    # Limita el movimiento del cuadro a la ventana
    if box.x > window_size[0] - box_size[0]:
        box.x = window_size[0] - box_size[0]
    if box.x < 0:
        box.x = 0
    if box.y > window_size[1] - box_size[1]:
        box.y = window_size[1] - box_size[1]
    if box.y < 0:
        box.y = 0

    # Rellena la ventana con un color
    screen.fill((0, 0, 0))

    # Dibuja el cuadro en la ventana
    pygame.draw.rect(screen, box_color, box)

    # Actualiza la pantalla
    pygame.display.flip()

    # Espera a que transcurra un tiempo
    pygame.time.delay(50)

