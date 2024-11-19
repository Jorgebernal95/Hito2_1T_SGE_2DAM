Hito 2 - SGE 2º DAM
Aplicación de Encuestas con Tkinter y MySQL

Descripción del Proyecto
Este proyecto permite gestionar encuestas relacionadas con el consumo de alcohol y su impacto en la salud. Utiliza Tkinter para la interfaz gráfica de usuario y MySQL para el almacenamiento y manipulación de datos. Además, incluye funcionalidades para analizar y visualizar los datos mediante gráficos.

Requisitos
Asegúrate de tener los siguientes elementos instalados antes de ejecutar la aplicación:

Python 3.x
Tkinter (viene preinstalado con Python en la mayoría de los casos)
MySQL
Librerías Python adicionales:
pymysql
pandas
matplotlib
openpyxl
Configuración Inicial
Crear la base de datos y la tabla
Ejecuta los siguientes comandos en tu gestor de base de datos MySQL:

sql
Copiar código
CREATE DATABASE ENCUESTAS;

USE ENCUESTAS;

CREATE TABLE ENCUESTA (
    idEncuesta INT PRIMARY KEY,
    edad INT,
    Sexo VARCHAR(10),
    BebidasSemana INT,
    CervezasSemana INT,
    BebidasFinSemana INT,
    BebidasDestiladasSemana INT,
    VinosSemana INT,
    PerdidasControl INT,
    DiversionDependenciaAlcohol VARCHAR(10),
    ProblemasDigestivos VARCHAR(10),
    TensionAlta VARCHAR(10),
    DolorCabeza VARCHAR(10)
);
Instalar dependencias
Usa pip para instalar las librerías necesarias:

bash
Copiar código
pip install pymysql pandas matplotlib openpyxl
Funcionalidades
Operaciones CRUD
Crear: Agrega nuevos registros a la base de datos a través de una ventana dedicada.
Leer: Visualiza todos los registros almacenados en la tabla.
Actualizar: Modifica datos de registros seleccionados.
Eliminar: Borra registros específicos de la base de datos.
Visualización de Gráficos
Consumo por Edad:
Muestra un gráfico de barras que representa el consumo de bebidas por grupos de edad.
Gráficos Personalizados:
Gráfico de Barras: Visualiza el consumo de bebidas según la edad.
Gráfico de Pastel: Muestra la distribución del consumo por sexo.
Promedios por Grupo de Edad:
Genera un gráfico de barras con los valores promedio de consumo de bebidas según grupos de edad.
Correlación Consumo-Salud:
Presenta un gráfico de dispersión para analizar la relación entre el consumo de alcohol y problemas digestivos.
Uso
Ejecuta el programa desde tu IDE o terminal.
Utiliza los botones de la interfaz para realizar las siguientes acciones:
Agregar Registro: Rellena el formulario y haz clic en "Agregar".
Actualizar Registro: Selecciona un registro, edita los datos y haz clic en "Actualizar".
Eliminar Registro: Selecciona un registro y haz clic en "Eliminar".
Visualizar Gráficos: Navega por las opciones disponibles para generar y analizar gráficos.
Capturas de Pantalla
(Opcional: Puedes incluir capturas de pantalla para mostrar la interfaz de usuario y los gráficos generados)

Autor
Proyecto desarrollado por [Tu Nombre] como parte del segundo curso de Desarrollo de Aplicaciones Multiplataforma.
