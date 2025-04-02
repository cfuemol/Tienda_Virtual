class Producto:
    """Generar la clase/objeto Producto que se usará cada vez 
        que se cree un producto nuevo.

        Es una clase de tipo básica
    """    
    def __init__(self, id_producto:str, nombre:str, precio:float, stock:int):
        """Constructor de la clase Producto, cada vez que creemos un producto,
            nos generará un objeto con los siguientes parámetros protegidos:

        :param id_producto: ID del producto
        :type id_producto: str
        :param nombre: Nombre del producto
        :type nombre: str
        :param precio: Precio del producto
        :type precio: float
        :param stock: Stock inicial del producto
        :type stock: int
        """        
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    ### GETTER y SETTER id_producto ###

    def get_id_producto(self):
        """Obtener ID Producto

        :return: ID del producto
        :rtype: str
        """        
        return self.__id_producto
    
    def set_id_producto(self, id_producto):
        """Modificar ID Producto

        :param id_producto: Nuevo ID del producto
        :type id_producto: str
        """        
        self.__id_producto = id_producto

    ### GETTER y SETTER nombre ###

    def get_nombre(self):
        """Obtener el nombre del producto

        :return: Nombre del producto
        :rtype: str
        """        
        return self.__nombre
    
    def set_nombre(self, nombre):
        """Modificar el nombre del producto

        :param nombre: Nuevo nombre del producto
        :type nombre: str
        """        
        self.__nombre = nombre

    ### GETTER y SETTER precio ###

    def get_precio(self):
        """Obtener el precio del producto

        :return: Precio del producto
        :rtype: float
        """        
        return self.__precio
    
    def set_precio(self, precio):
        """Modificar el precio del producto

        :param precio: Nuevo precio del producto
        :type precio: float
        """        
        self.__precio = precio

    ### GETTER y SETTER stock ###

    def get_stock(self):
        """Obtener el stock del producto

        :return: Stock del producto
        :rtype: int
        """        
        return self.__stock
    
    def set_stock(self, stock):
        """Modificar el stock del producto

        :param stock: Nuevo stock del producto
        :type stock: int
        """        
        self.__stock = stock

    ### Construimos la impresión por pantalla ###

    def __str__(self):
        """Establecer el formato de impresión por pantalla

        :return: La información del producto solicitado
        :rtype: str
        """        
        return f'\n- Código: {self.__id_producto}\n- Nombre: {self.__nombre}\n- Precio: {self.__precio} €\n- Stock: {self.__stock} unidades'
    
    ### Método para actualizar el stock ###

    def actualizar_stock(self, stock):
        """Actualizar stock

        :param stock: Nuevo stock del producto
        :type stock: int
        :return: Nuevo valor del stock del producto
        :rtype: int
        """        
        self.set_stock(stock)
        return f'{self.__nombre} tiene de stock {self.__stock} unidades'
    