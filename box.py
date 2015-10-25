
class box(object):

    RETICULADO = 0.1
    WIDTH = 10
    LENGTH = 15

    ''' Variables que almacenan los indices del centro '''
    N_x0 = []
    N_y0 = []

    ''' Arreglo con la caja '''
    box = []


    def __init__(self):

        self.create_box()
        self.set_center()


    def create_box( self ):
        ''' Crea una caja llena de ceros de 10 x 15 cm, reticulado 0.1 cm '''

        N_x = int( self.WIDTH / self.RETICULADO )
        N_y = int( self.LENGTH / self.RETICULADO )

        assert N_x * self.RETICULADO == self.WIDTH , 'Eje X no se puede dividir en numero entero de celdas'
        assert N_y * self.RETICULADO == self.LENGTH , 'Eje Y no se puede dividir en numero entero de celdas'

        for x in range( N_x ):
            self.box.append([])
            for y in range( N_y ):
                self.box[-1].append(0)


    def set_center( self ):
        ''' Calcula el centro de una matriz 2D
        con numero de indices x e y '''

        x_size = len( self.box )
        y_size = len( self.box[0] )

        self.N_x0 = int( x_size / 2 )
        self.N_y0 = int( y_size / 2 )


    def coord( self, x_cm , y_cm):
        ''' Convierte una posicion en cm a posicion en indices de box '''

        assert -self.WIDTH / 2 <= x_cm < self.WIDTH / 2, 'Posicion x fuera de matriz'
        assert -self.LENGTH / 2 <= x_cm < self.LENGTH / 2, 'Posicion y fuera de matriz'

        Nx_box = self.N_x0 + int( x_cm / self.RETICULADO )
        Ny_box = self.N_y0 + int( y_cm / self.RETICULADO )

        return Nx_box, Ny_box

    def draw_block(self, x_origin, y_origin , x_size , y_size , density_per_cm2 ):
        ''' Llena bloque de x_size x y_size [cm] con densidad density_per_cm2
        x_origin, y_origin son las coordenadas del vertice inferior izquierdo del bloque'''

        N_x , N_y = self.coord( x_origin , y_origin )

        largo_trazo_x = x_size / self.RETICULADO
        largo_trazo_y = y_size / self.RETICULADO
        largo_cm = 1 / self.RETICULADO # Permite ajustar densidad a reticulado

        assert largo_trazo_x % 1 == 0, 'Bloque de dibujo tiene lado x con indice no entero'
        assert largo_trazo_y % 1 == 0, 'Bloque de dibujo tiene lado y con indice no entero'
        assert largo_cm % 1 == 0, 'Bloque de 1x1 tiene indices no enteros'

        density_adj = density_per_cm2 / ( largo_cm ** 2 )

        # Convertir indice final a entero
        N_x_end = int(N_x + largo_trazo_x)
        N_y_end = int(N_y + largo_trazo_y)

        for i in range( N_x , N_x_end ):
            for j in range( N_y , N_y_end ):
                self.box[i][j] = density_adj


    def draw_letter( self ):
        ''' Dibuja una letra F dentro de un rectangulo centrado de 5 x 7 cm
        Area letra F = 23 cm^2
        Carga total = 1 [C] '''

        ancho = 5.0
        largo = 7.0

        ''' CORREGIR: Buscar forma de diferenciar voltajes de densidad de carga en la matriz'''
        dens_carga = 1.0 / 23.0

        ''' Esquina inferior letra '''
        x_inf = -ancho/2
        y_inf = -largo/2

        ''' Dibujar letra usando bloques (Arte) '''
        self.draw_block(x_inf , y_inf , 2 , 7 , dens_carga )
        self.draw_block(x_inf + 2, y_inf + 3, 3 , 1 , dens_carga )
        self.draw_block(x_inf + 2, y_inf + 5, 3 , 2 , dens_carga )


    # END of create_letter


    def get_box(self):
        return self.box
