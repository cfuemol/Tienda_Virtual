class Cliente:
    """Generar la clase/objeto Cliente que se usará cada vez 
        que se cree un cliente nuevo.

        Es una clase de tipo básica
    """
    def __init__(self, id_cliente:str, nombre:str, email:str, direccion:str):
        """Constructor de la clase Cliente, cada vez que creemos un cliente,
            nos generará un objeto con los siguientes parámetros protegidos:

        :param id_cliente: ID del cliente
        :type id_cliente: str
        :param nombre: Nombre del cliente
        :type nombre: str
        :param email: Email del cliente
        :type email: str
        :param direccion: Dirección del cliente
        :type direccion: str
        """
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__email = email
        self.__direccion = direccion

    ### GETTER y SETTER id_cliente ###

    def get_id_cliente(self):
        """Obtener el ID del cliente

        :return: ID del cliente
        :rtype: str
        """        
        return self.__id_cliente
    
    def set_id_cliente(self, id_cliente):
        """Modificar el ID del cliente

        :param id_cliente: Nuevo ID del cliente
        :type id_cliente: str
        """        
        self.__id_cliente = id_cliente

    ### GETTER y SETTER nombre ###

    def get_nombre(self):
        """Obtener el nombre del cliente

        :return: Nombre del cliente
        :rtype: str
        """        
        return self.__nombre
    
    def set_nombre(self, nombre):
        """Modificar el nombre del cliente

        :param nombre: Nuevo nombre del cliente
        :type nombre: str
        """        
        self.__nombre = nombre

    ### GETTER y SETTER email ###

    def get_email(self):
        """Obtener el email del cliente

        :return: Email del cliente
        :rtype: str
        """        
        return self.__email
    
    def set_email(self, email):
        """Modificar el email del cliente

        :param email: Nuevo email del cliente
        :type email: str
        """        
        self.__email = email

    ### GETTER y SETTER direccion ###

    def get_direccion(self):
        """Obtener la dirección del cliente

        :return: Dirección del cliente
        :rtype: str
        """        
        return self.__direccion
    
    def set_direccion(self, direccion):
        """Modificar la dirección del cliente

        :param direccion: Nueva dirección del cliente
        :type direccion: str
        """        
        self.__direccion = direccion

    ### Construimos la impresión por pantalla ###

    def __str__(self):
        """Establecer el formato de impresión por pantalla

        :return: La información del cliente solicitado
        :rtype: str
        """        
        return f'\n- Código: {self.__id_cliente}\n- Nombre: {self.__nombre}\n- Email: {self.__email}\n- Dirección: {self.__direccion}'