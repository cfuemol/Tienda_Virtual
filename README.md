# Tienda_Virtual

## IES Abdera (Adra - Almería)
### CFGS Desarrollo de Aplicaciones Web (DAW)
#### Curso 2024 - 2025

---

## 1. Introducción
Bienvenido/a a este proyecto cuyo objetivo es agilizar la gestión de una tienda.  
El objetivo es que sea fácil de utilizar tanto para gestionar la tienda de forma física como de forma online y realizar ventas.

---

## 2. Instalación
Pasos detallados para instalar y configurar la aplicación.

**Requisitos previos:**
- Instalación de Python en la version 3.12 o superior (sin importar si es para Windows, Linux o MacOS)  
- Instalación de dependencias si es necesario
- Manejar desde terminal de comandos  

**Instalación Paso a Paso:**
1. Clonar el repositorio desde `https://github.com/cfuemol/Tienda_Virtual.git`  
2. Acceder al directorio del proyecto:  
   ```bash
   cd Tienda_Virtual
   ```  
3. Acceder a la aplicación desde la terminal de comandos:
    ```bash
   cd project
   python3 main.py
   ```

---

## 3. Funcionalidades del Software
1. Gestionar productos (Identificando si son físicos o digitales)
2. Gestionar clientes
3. Gestionar pedidos
4. Gestionar reseñas (De productos ya comprados por el cliente)

### 3.1 Gestionar productos
- Gestionar productos que tenemos en tienda, almacenados en una lista

```plaintext
🔹 Añadir un producto: nos pedirá los datos que queremos almacenar, así como si es físico o digital
🔹 Listar productos: nos muestra por pantalla los productos que tengamos registrados junto con sus datos
🔹 Actualizar stock: nos permite cambiar el stock que tenemos de un producto
```

### 3.2 Gestionar clientes
- Gestionar cliente que tenemos registrados, almacenados en un diccionario

```plaintext
🔹 Añadir un cliente: nos pedirá los datos que queremos almacenar
🔹 Listar clientes: nos muestra por pantalla los clientes que tengamos registrados junto con sus datos
```

### 3.3 Gestionar pedidos
- Gestionar pedidos realizados, almacenados en una lista

```plaintext
🔹 Crear pedido: nos pedirá id_pedido e id_cliente para crearlo, en caso contrario dará error
🔹 Añadir producto: nos permite añadir un producto existente en nuestra lista de productos al pedido
🔹 Listar pedidos: nos muestra por pantalla los pedidos que tenemos registrados
🔹 Calcular total: nos muestra por pantalla el valor del pedido que le introduzcamos por teclado mediante el id_pedido
```

---

## 4. Preguntas Frecuentes (FAQ)
**❓ Da errores arbitarios**  
- Cerrar el programa y volverlo a ejecutar  

**❓ ¿El programa no hace validaciones de datos?**  
- Se implementará en futuras versiones, así como la persistencia de datos 

---

## 5. Contacto y Soporte
- Email de soporte: `soporte@iesabdera.com`  
- Teléfono de contacto: `950 XXX XXX`  

---

## 6. Créditos y Licencia
- El desarrollador de esta APP es un estudiante de 1° DAW 
- Aplicación amparada bajo el estandar GNU General Public License v.3.0

---
