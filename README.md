# Hito 2 - SGE 2º DAM: Aplicación de Encuestas con Tkinter y MySQL
## Descripción del Proyecto
Este proyecto gestiona encuestas relacionadas con el consumo de alcohol y su relación con problemas de salud. 
Combina:

Tkinter para la interfaz gráfica de usuario
MySQL para el almacenamiento y manipulación de datos
Herramientas para visualizar datos mediante gráficos

## Requisitos
Antes de ejecutar la aplicación, asegúrate de contar con:

Python 3.x
Tkinter (preinstalado con Python en la mayoría de los casos)
MySQL

## Las siguientes librerías adicionales:

pymysql
pandas
matplotlib
openpyxl



## Configuración Inicial
Base de datos y tabla
Configura la base de datos ejecutando los siguientes comandos en tu gestor MySQL:
sqlCopyCREATE DATABASE ENCUESTAS;

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
## Instalar dependencias
Ejecuta este comando en la terminal para instalar las librerías necesarias:
bashCopypip install pymysql pandas matplotlib openpyxl
## Funcionalidades
## Operaciones CRUD

Crear: Permite agregar nuevos registros mediante un formulario interactivo
Leer: Muestra todos los registros almacenados en la base de datos
Actualizar: Permite modificar registros existentes seleccionados
Eliminar: Elimina registros seleccionados de la base de datos

## Visualización de Gráficos

Consumo por Edad: Gráfico de barras que muestra el consumo promedio por grupo de edad
Gráficos Personalizados:

Gráfico de barras con consumo por edad
Gráfico de pastel con la distribución por sexo


Promedios por Grupo de Edad: Genera un gráfico de barras mostrando el promedio de consumo en diferentes grupos de edad
Correlación Consumo-Salud: Genera un gráfico de dispersión que analiza la relación entre consumo de alcohol y problemas de salud

## Uso

Ejecuta el programa desde tu entorno de desarrollo o terminal
Usa los botones en la interfaz para interactuar con la base de datos:

Agregar Registro: Completa el formulario y guarda un nuevo registro
Leer Registros: Muestra todos los registros almacenados
Actualizar Registro: Edita los datos de un registro existente
Eliminar Registro: Borra un registro seleccionado



