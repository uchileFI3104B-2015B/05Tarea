
''' Calculo de potencial electrostatico en caja cerrada
de tamano 10 x 15 [cm], reticulado de 0.2 [cm]
uso: solv_poisson.py
'''

RETICULADO = 0.2
WIDTH = 10
LENGTH = 15




def create_box():
    ''' Crea una caja vacia de 10 x 15 cm '''
    N_x = WIDTH / RETICULADO
    N_y = LENGTH / RETICULADO

    assert N_x * RETICULADO == WIDTH, 'Caja con ancho distinto de 10 [cm]'
    assert N_y * RETICULADO == LENGTH, 'Caja con largo distinto de 15 [cm]'

    box = []

    for x in range( N_x ):
        box.append([])
        for y in range( N_y ):
            box[-1].append([])

    return box


def get_center(box):
    ''' Retorna los indices del centro de box.
    Si box tiene una de sus dimensiones de tamano par,
    se usa el termino inmediatamente anterior al centro teorico '''

    a = 1 # IMPLEMENTAR PLAS

def draw_letter(box):
    ''' Dibuja la letra F dentro de un rectangulo centrado de 5 x 7 [cm] con grosor de lineas de 1 [cm]
    LLena las lineas con densidad de carga tal que el total sea 1 [C]
    Retorna los indices de box ocupados por la letra'''

    x_center, y_center = get_center(box)
    assert x_center, 'No se encontro x central'
    assert y_center, 'No se encontro y central'

    

# Main driver
if __name__ == '__main__':
    # Crear caja vacia
    box = create_box()

    # Escribir letra F
    draw_letter(box)

    # Escribir condiciones de borde constantes
    # Escribir condicion de borde derivativa
    # Resolver
    # Presentar resultados
