from productos import Producto

class ProductoDigital(Producto):
    """Generar la clase/objeto ProductoDigital que se usará cada vez 
        que se cree un producto digital nuevo.

        Es una clase derivada de Producto

    :param Producto: Datos del producto
    :type Producto: object
    """    
    def __init__(self, id_producto:str, nombre:str, precio:float, stock:int, formato:str, tamano:str):
        """Constructor de la clase ProductoDigital, cada vez que creemos un producto digital,
            nos generará un objeto con los siguientes parámetros protegidos:

        :param id_producto: _description_
        :type id_producto: str
        :param nombre: _description_
        :type nombre: str
        :param precio: _description_
        :type precio: float
        :param stock: _description_
        :type stock: int
        :param formato: _description_
        :type formato: str
        :param tamano: _description_
        :type tamano: str
        """        

        super().__init__(id_producto, nombre, precio, stock)
        """Heredará de la clase Producto los atributos
        """        
        self.__formato = formato
        self.__tamano = tamano

    ### GETTER y SETTER formato ###

    def get_formato(self):
        """Obtener el formato del producto digital

        :return: Obtener el formato del producto digital
        :rtype: str
        """        
        return self.__formato
    
    def set_formato(self, formato):
        """Modificar el formato del producto digital

        :param formato: Modificar el formato del producto digital
        :type formato: str
        """        
        self.__formato = formato

    ### GETTER y SETTER tamaño ###

    def get_tamano(self):
        """Obtener el tamaño del producto digital

        :return: Obtener el tamaño del producto digital
        :rtype: str
        """        
        return self.__tamano
    
    def set_tamano(self, tamano):
        """Modificar el tamaño del producto digital

        :param tamano: Modificar el tamaño del producto digital
        :type tamano: str
        """        
        self.__tamano = tamano

    ### Construir el str (Se reconstruye el del padre porque nos vale) ###

    def __str__(self):
        """Establecer el formato de impresión por pantalla

        :return: Datos del producto + datos de producto digital
        :rtype: str
        """        
        return f' {super().__str__()}\n- Formato: {self.__formato}\n- Tamaño: {self.__tamano}' 
