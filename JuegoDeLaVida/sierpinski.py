import turtle
import time
import random

def inicializar_fila(n):
    """
    Crea una fila inicial con una celda activada en el centro.
    """
    fila = [0] * n
    fila[n // 2] = 1
    return fila

def siguiente_fila(fila):
    """
    Calcula la siguiente fila del triángulo según la Regla 90.
    """
    nueva_fila = [0] * len(fila)
    for i in range(1, len(fila) - 1):
        # Regla 90: XOR de las dos celdas vecinas
        nueva_fila[i] = fila[i - 1] ^ fila[i + 1]
    return nueva_fila

def dibujar_trazo(t, x, y, longitud):
    """
    Dibuja un trazo horizontal en la posición (x, y) con la longitud especificada.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(longitud)

def generar_triangulo_sierpinski(t, filas, ancho, cell_size):
    """
    Genera y dibuja el Triángulo de Sierpinski como trazos desde la base a la punta.
    """
    fila_actual = inicializar_fila(ancho)
    x_start = -(ancho // 2) * cell_size  # Centrar el triángulo en el eje X

    for y in range(filas):
        # Elegimos un color aleatorio para cada fila
        t.color(random.random(), random.random(), random.random())
        
        for x, cell in enumerate(fila_actual):
            if cell == 1:
                # Calculamos la posición del inicio del trazo
                x_pos = x_start + x * cell_size
                y_pos = - y * cell_size  # Y negativa para dibujar hacia arriba
                dibujar_trazo(t, x_pos, y_pos, cell_size)  # Dibuja el trazo horizontal
                time.sleep(0.03)  # Pausa breve para ver el trazo aparecer gradualmente
        fila_actual = siguiente_fila(fila_actual)

# Parámetros
filas = 20         # Número de filas para el triángulo
ancho = 41         # Ancho de la matriz, debe ser impar para mejor alineación
cell_size = 15     # Longitud de cada trazo en píxeles

# Configuración de Turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)  # Ancho del trazo para un efecto de pincelada
t.hideturtle()
turtle.bgcolor("white")
turtle.title("Triángulo de Sierpinski - Autómata Celular")

# Centrar el triángulo en la ventana Turtle
turtle.setup(width=ancho * cell_size + 40, height=filas * cell_size + 40)

# Dibujar el Triángulo de Sierpinski
generar_triangulo_sierpinski(t, filas, ancho, cell_size)

# Terminar
turtle.done()
