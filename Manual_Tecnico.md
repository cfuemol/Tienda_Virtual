# Manual Técnico del Proyecto Tienda_Virtual
## IES Abdera (Adra - Almería)
### CFGS Desarrollo de Aplicaciones Web (DAW)
#### Curso 2024 - 2025

---

## 1. Información General
- **Nombre del Proyecto** Tienda Virtual
- **Autor** Cristóbal Fuentes
- **Fecha de Creación** 10/04/2025
- **Última Actualización** 10/04/2025
- **Profesor Responsable** José Ramón Rivas

--

## 2. Descripción del Proyecto
La APP pretender ayudar al responsable de un establecimiento en el correcto desempeño de su negocio.
Para ello permitirá registrar tanto a clientes como a productos, permitiéndole a los usuarios generar pedidos y hacer reseñas de los productos obtenidos.

---

## 3. Tecnologías Utilizadas
Listado de tecnologías empleadas en el desarrollo:
- **Frontend:** No se ha utilizado ninguna  
- **Backend:** Python puro  
- **Base de Datos:** No utilizadas en este proyecto  
- **Control de Versiones:** En la elaboración no se ha realizado ningún control de versiones, se trata de una demo demostrativa para potenciales clientes  
- **Despliegue:** Ninguno, se ejecuta de manera local
  

---

## 4. Requisitos Previos
Lista de software necesario para ejecutar el proyecto:  
- Python 3.12 de 64-bits y sus dependencias
- Visual Studio Code o consola de comandos 

---

## 5. Estructura del Proyecto

```plaintext

📂 Tienda_Virtual
├── Casos_Uso.png
├── Diagrama_Clases.png
├── Manual_Tecnico.md
├── Manual_Usuario.md
├── README.md
├── 📂 docs
│   ├── Makefile
│   ├── 📂 build
│   │   ├── 📂 doctrees
│   │   │   ├── environment.pickle
│   │   │   ├── index.doctree
│   │   │   ├── modules.doctree
│   │   │   └── project.doctree
│   │   └── 📂 html
│   │       ├── 📂 _modules
│   │       │   ├── index.html
│   │       │   └── 📂 project
│   │       │       ├── clientes.html
│   │       │       └── productos.html
│   │       ├── 📂 _sources
│   │       │   ├── index.rst.txt
│   │       │   ├── modules.rst.txt
│   │       │   └── project.rst.txt
│   │       ├── 📂 _static
│   │       │   ├── alabaster.css
│   │       │   ├── base-stemmer.js
│   │       │   ├── basic.css
│   │       │   ├── custom.css
│   │       │   ├── doctools.js
│   │       │   ├── documentation_options.js
│   │       │   ├── file.png
│   │       │   ├── forkme_right_darkblue_121621.png
│   │       │   ├── language_data.js
│   │       │   ├── minus.png
│   │       │   ├── plus.png
│   │       │   ├── pygments.css
│   │       │   ├── searchtools.js
│   │       │   ├── spanish-stemmer.js
│   │       │   ├── sphinx_highlight.js
│   │       │   └── translations.js
│   │       ├── genindex.html
│   │       ├── index.html
│   │       ├── modules.html
│   │       ├── objects.inv
│   │       ├── project.html
│   │       ├── py-modindex.html
│   │       ├── search.html
│   │       └── searchindex.js
│   ├── make.bat
│   └── 📂 source
│       ├── conf.py
│       ├── index.rst
│       ├── modules.rst
│       └── project.rst
└── 📂 project
    ├── __init__.py
    ├── 📂 __pycache__
    │   ├── __init__.cpython-312.pyc
    │   ├── clientes.cpython-312.pyc
    │   ├── main.cpython-312.pyc
    │   ├── menu.cpython-312.pyc
    │   ├── pedido.cpython-312.pyc
    │   ├── producto_digital.cpython-312.pyc
    │   ├── productos.cpython-312.pyc
    │   └── reseña.cpython-312.pyc
    ├── clientes.py
    ├── main.py
    ├── menu.py
    ├── pedido.py
    ├── producto_digital.py
    ├── productos.py
    └── reseña.py
```


---

## 6. Instalación y Configuración

Instalar Python, funciona en Windows, Linux y MacOS.

(Opcional) Instalar Visual Studio Code para ejecutarlo o hacerlo desde la terminal con el comando python3 + nombre del archivo .py

---

## 7. Base de Datos
- En el proyecto no se utiliza ninguna base de datos, es una funcionalidad pendiente de implementar en un futuro

---

## 8. API y Endpoints
No se realizan Endpoints por tratarse de una APP que se ejecuta de forma local y sin persistencia de datos mediante una Base de Datos, se implementará en un futuro dicha funcionalidad

---

## 9. Seguridad
- Validaciones de entrada de datos, pendiente de realizar  
 

---

## 10. Configuración del Servidor Web
Al ser una APP de ejecución local no necesita despliéguelas, en un futuro se implementará dicha función 

---

## 11. Pruebas y Debugging
Las pruebas realizadas se hacen con datos introducidos manualmente mediante durante la ejecución del programa   

---

## 12. Uso de Inteligencia Artificial
No se ha realizado ningún uso de la IA en la realización de este proyecto 

---

## 13. Despliegue en Producción
Proyecto no desplegado, será una funcionalidad futura para darle versatilidad  

---

## 14. Conclusión
- El desarrollo del proyecto siguió las pautas de aprendizaje de Python con respecto a la programación orientada a objetos (POO), por ello las instrucciones pueden pecar de ser "simples" 
- Dentro de las mejoras a implementar, que son bastantes, nos quedaremos con convertir este proyecto en una APP completa con todos sus elementos, que se pueda utilizar con concurrencia de usuarios y con el despliegue necesario para tal fin  

---

## 15. Créditos y Referencias
- Fuentes utilizadas: Apuntes facilitados por el profesorado y diversos tutoriales presentes en la web  
- Créditos a colaboradores: Al profesorado y los alumnos de 1° DAW del IES Abdera, su ayuda fue inestimable para la construcción de este proyecto  

---
