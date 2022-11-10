"""
    Este el archivo encargado de las funcionalidades del carrito de compras
"""

class Carro:
    # Constructor del carrito de compras:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        carro = self.session.get('carro')

        # Validación que exista el carrito:
        if not carro:
            carro = self.session['carro'] = {}
        self.carro = carro

    # Métodos propios del carrito:
    def agregarProducto(self, producto):
        """Agregar productos al carro"""
        # Validar si el producto ya existe en el carrito:
        if(str(producto.id) not in self.carro.keys()):          # Si el producto no se encuentra en el carro, agregar:
            self.carro[producto.id] = {                         # Creamos un diccionario con los atributos del producto, y este
                "producto_id" : producto.id,                    # se guarda por id, es decir por cada producto creamos esta 
                "nombre" : producto.nombre_producto,            # estructura
                "precio" : str(producto.valor_venta),           # El campo precio lo pasamos como str, 
                "cantidad": 1,
                "subtotal": 1,
                "imagen" : producto.imagen_producto.url
            }
        else:
            # Si ya hay un producto actualizamos la cantidad de ese producto:
            for key, value in self.carro.items():               # Recorremos todos los items del carrito   
                if key == str(producto.id):                     # Si encontramos un producto que tiene ese id
                    value['cantidad'] = value['cantidad'] + 1   # Sumamos el valor de la clave cantidad
                    value['subtotal'] = float(producto.valor_venta)  * float(value['cantidad'])
                    break                                       # Terminamos abruptamente el proceso
        # Por último guardamos el carrito de compras:
        self.guadarCarro()
    
    def guadarCarro(self):
        """Guardar el carro cuando se actualice """
        self.session['carro'] = self.carro                      # Guardamos en la variable session, el objeto carro
        self.session.modified = True                            # Asignamos el cambio de modificacion.

    def eliminarProducto(self, producto):
        """Eliminar productos al carro"""
        producto.id = str(producto.id)                          # Convertimos en string el producto id, porque es la clave de nuestro objeto
        if producto.id in self.carro:                           # Si esta clave se encuentra en el objeto carro
            del self.carro[producto.id]                         # Eliminamos esta clave del objeto
            self.guadarCarro()                                  # Actualizamos el carrito de compras

    def restarProducto(self, producto):
        """Restar unidades de productos del carro"""
        for key, value in self.carro.items():
            if key == str(producto.id):
                value['cantidad'] = value['cantidad'] - 1
                value['subtotal'] = float(value['precio'])  * float(value['cantidad'])
                if value['cantidad'] < 1:
                    self.eliminarProducto(producto)
                break
        self.guadarCarro()

    def limpiarCarro(self):
        """Vaciar todos los productos del carro"""
        carro = self.session['carro'] = {}
        self.session.modified = True
        