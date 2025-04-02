from clientes import Cliente

class Pedido:
    """Generar la clase/objeto Pedido que se usará cada vez 
        que se cree un pedido nuevo.

        Es una clase de tipo básica
    """    
    def __init__(self, id_pedido:str, cliente: Cliente, fecha:str):
        """Constructor de la clase Pedido, cada vez que creemos un pedido,
            nos generará un objeto con los siguientes parámetros protegidos 

        :param id_pedido: ID del pedido
        :type id_pedido: str
        :param cliente: Datos del cliente
        :type cliente: Cliente
        :param fecha: Fecha en la que se realiza el pedido
        :type fecha: str
        """        
        self.__id_pedido = id_pedido
        self.__cliente = cliente
        self.__productos = []
        self.__fecha = fecha

    ### GETTER y SETTER para id_pedido ###
    def get_id_pedido(self):
        """Obtener ID del pedido

        :return: ID del pedido
        :rtype: str
        """        
        return self.__id_pedido
    
    def set_id_pedido(self, id_pedido):
        """Modificar ID del pedido

        :param id_pedido: ID del pedido
        :type id_pedido: str
        """        
        self.__id_pedido = id_pedido

    ### GETTER y SETTER para cliente ###
    def get_cliente(self):
        """Obtener los datos del cliente

        :return: Los datos del cliente
        :rtype: object
        """        
        return self.__cliente
    
    def set_cliente(self, cliente):
        """Modificar los datos del cliente

        :param cliente: Datos del cliente
        :type cliente: object
        """        
        self.__cliente = cliente

    ### GETTER y SETTER para fecha ###
    def get_fecha(self):
        """Obtener fecha del pedido

        :return: Fecha en la que se realiza el pedido
        :rtype: str
        """        
        return self.__fecha
    
    def set_fecha(self, fecha):
        """Modificar la fecha de realización del pedido

        :param fecha: Nueva fecha de realización del pedido
        :type fecha: str
        """        
        self.__fecha = fecha

    ### GETTER para lista productos ###
    def get_lista_productos(self):
        """Obtener lista de productos registrados 

        :return: Lista de productos registrados
        :rtype: list
        """        
        return self.__productos

    ### Agregar productos ###
    def agregar_producto(self, producto:object):
        """Agregar productos al carrito

        :param producto: Producto añadido al carrito
        :type producto: object
        """        
        self.__productos.append(producto)

    ### Calcular el total del pedido ###
    def calcular_total(self):
        """Calcular el total del carrito

        :return: Valor del carrito
        :rtype: float
        """        
        suma = 0.0
        for producto in self.__productos:
            suma += producto.get_precio()

        return suma

    ### Construimos el str ###

    def __str__(self):
        """Establecer el formato de impresión por pantalla

        :return: _La información del pedido solicitado
        :rtype: str
        """        
        return f'\n- Pedido: {self.__id_pedido}\n- Cliente: {self.__cliente.get_nombre()}\n- Fecha: {self.__fecha}\n- Lista Productos: {self.__productos}'    