from clientes import Cliente
from productos import Producto

class Reseña(Producto, Cliente):
    """Generar la clase/objeto Producto que se usará cada vez 
        que se cree un producto nuevo.

        Es una clase derivada de Producto y Cliente

        :param Producto: Datos del producto
        :type Producto: object
        :param Cliente: Datos del cliente
        :type Producto: object
    """    
    def __init__(self, id_reseña:str, producto:Producto, cliente:Cliente, comentario:str):
        """_summary_

        :param id_reseña: ID de la reseña
        :type id_reseña: str
        :param producto: Datos del producto
        :type producto: Producto
        :param cliente: Datos del cliente
        :type cliente: Cliente
        :param comentario: Comentario introducido
        :type comentario: str
        """        
        Producto.__init__(self, producto.get_id_producto(), producto.get_nombre(), producto.get_precio(), producto.get_stock())
        Cliente.__init__(self, cliente.get_id_cliente(), cliente.get_nombre(), cliente.get_email(), cliente.get_direccion())
        self.__id_reseña = id_reseña
        self.__comentario = comentario
        self.__puntuacion = None

    ### GETTER y SETTER para id_reseña ###

    def get_id_reseña(self):
        """Obtener el ID de la reseña

        :return: ID de la reseña
        :rtype: str
        """        
        return self.__id_reseña
    
    def set_id_reseña(self, id_reseña):
        """Modificar el ID_reseña
        """        
        self.__id_reseña = id_reseña

    ### GETTER y SETTER para comentario ###

    def get_comentario(self):
        """Obtener el comentario

        :return: Comentario introducido por el usuario
        :rtype: str
        """        
        return self.__comentario
    
    def set_comentario(self, comentario):
        """Modificar el comentario introducido por el usuario

        :param comentario: Nuevo comentario
        :type comentario: str
        """        
        self.__comentario = comentario

    ### GETTER y SETTER para puntuacion ###

    def get_puntuacion(self):
        """Obtener la puntuación otorgada por el usuario

        :return: Puntuación otorgada por el usuario
        :rtype: float
        """        
        return self.__puntuacion
    
    def set_puntuacion(self, puntuacion):
        """Modificación de la puntuación otorgada por el usuario

        :param puntuacion: Nueva puntuación
        :type puntuacion: float
        """        
        self.__puntuacion = puntuacion

    ### Construimos el str ###

    def __str__(self):
        """Establecer el formato de impresión por pantalla

        :return: Datos de la reseña + datos de producto + datos del cliente
        :rtype: str
        """         
        return f'\n- ID_Reseña: {self.__id_reseña}\n- Producto: {self.get_id_producto()}\n- ID_Cliente: {self.get_id_cliente()}\n- Puntuación: {self.__puntuacion}\n- Comentario: {self.__comentario}' 