class Cliente:
    """_summary_

    ### Parámetros
    1. id_cliente: str
        - Código de identifiación del cliente
    2.- nombre: str
        - Nombre del cliente
    3.- email: str
        - Email del cliente
    4.- direccion: str
        - Dirección del cliente
    """    
    def __init__(self, id_cliente:str, nombre:str, email:str, direccion:str):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__email = email
        self.__direccion = direccion

    ### GETTER y SETTER id_cliente ###

    def get_id_cliente(self):
        return self.__id_cliente
    
    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    ### GETTER y SETTER nombre ###

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    ### GETTER y SETTER email ###

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    ### GETTER y SETTER direccion ###

    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self, direccion):
        self.__direccion = direccion

    ### Construimos la impresión por pantalla ###

    def __str__(self):
        return f'\n- Código: {self.__id_cliente}\n- Nombre: {self.__nombre}\n- Email: {self.__email}\n- Dirección: {self.__direccion}'