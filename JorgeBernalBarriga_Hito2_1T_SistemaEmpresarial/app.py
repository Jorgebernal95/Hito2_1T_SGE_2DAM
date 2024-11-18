import tkinter as tk
from tkinter import ttk, messagebox
from database import leer_registros, insertar_registro, actualizar_registro, eliminar_registro
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Encuestas")
root.geometry("1200x600")

# Estilo para los widgets
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10, background="#4CAF50")
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))

# Título de la aplicación
titulo = ttk.Label(root, text="Sistema de Gestión de Encuestas", font=("Helvetica", 16, "bold"))
titulo.pack(pady=10)

# Variable global para almacenar registros filtrados
registros_filtrados = []

# Función para actualizar la tabla de datos
def actualizar_tabla(filtro=None):
    global registros_filtrados
    try:
        for row in tree.get_children():
            tree.delete(row)
        registros = leer_registros()
        if filtro:
            registros = list(filter(filtro, registros))
        registros_filtrados = registros  # Almacenar registros filtrados
        for registro in registros:
            tree.insert("", "end", values=registro)
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar la tabla: {e}")

# Función para mostrar la ventana de creación de registros
def mostrar_ventana_crear():
    ventana_crear = tk.Toplevel(root)
    ventana_crear.title("Crear Registro")
    ventana_crear.geometry("400x600")

    frame_entrada = ttk.Frame(ventana_crear, padding=10)
    frame_entrada.pack(pady=10)

    labels = ["ID Encuesta", "Edad", "Sexo", "Bebidas Semana", "Cervezas Semana", "Bebidas Fin Semana", "Bebidas Destiladas Semana", "Vinos Semana", "Perdidas Control", "Diversion Dependencia Alcohol", "Problemas Digestivos", "Tension Alta", "Dolor Cabeza"]
    entries = []

    for i, label in enumerate(labels):
        ttk.Label(frame_entrada, text=label).grid(row=i, column=0, sticky=tk.W, pady=5)
        entry = ttk.Entry(frame_entrada)
        entry.grid(row=i, column=1, pady=5)
        entries.append(entry)

    id_entrada, edad_entrada, sexo_entrada, bebidas_semana_entrada, cervezas_semana_entrada, bebidas_fin_semana_entrada, bebidas_destiladas_semana_entrada, vinos_semana_entrada, perdidas_control_entrada, diversion_dependencia_alcohol_entrada, problemas_digestivos_entrada, tension_alta_entrada, dolor_cabeza_entrada = entries

    def agregar_registro():
        datos = (
            id_entrada.get(),
            edad_entrada.get(),
            sexo_entrada.get(),
            bebidas_semana_entrada.get(),
            cervezas_semana_entrada.get(),
            bebidas_fin_semana_entrada.get(),
            bebidas_destiladas_semana_entrada.get(),
            vinos_semana_entrada.get(),
            perdidas_control_entrada.get(),
            diversion_dependencia_alcohol_entrada.get(),
            problemas_digestivos_entrada.get(),
            tension_alta_entrada.get(),
            dolor_cabeza_entrada.get()
        )
        insertar_registro(datos)
        actualizar_tabla()
        ventana_crear.destroy()

    btn_agregar = ttk.Button(ventana_crear, text="Agregar Registro", command=agregar_registro)
    btn_agregar.pack(pady=10)

# Función para mostrar la ventana de actualización de registros
def mostrar_ventana_actualizar():
    ventana_actualizar = tk.Toplevel(root)
    ventana_actualizar.title("Actualizar Registro")
    ventana_actualizar.geometry("400x600")

    frame_entrada = ttk.Frame(ventana_actualizar, padding=10)
    frame_entrada.pack(pady=10)

    labels = ["ID Encuesta", "Edad", "Sexo", "Bebidas Semana", "Cervezas Semana", "Bebidas Fin Semana", "Bebidas Destiladas Semana", "Vinos Semana", "Perdidas Control", "Diversion Dependencia Alcohol", "Problemas Digestivos", "Tension Alta", "Dolor Cabeza"]
    entries = []

    for i, label in enumerate(labels):
        ttk.Label(frame_entrada, text=label).grid(row=i, column=0, sticky=tk.W, pady=5)
        entry = ttk.Entry(frame_entrada)
        entry.grid(row=i, column=1, pady=5)
        entries.append(entry)

    id_entrada, edad_entrada, sexo_entrada, bebidas_semana_entrada, cervezas_semana_entrada, bebidas_fin_semana_entrada, bebidas_destiladas_semana_entrada, vinos_semana_entrada, perdidas_control_entrada, diversion_dependencia_alcohol_entrada, problemas_digestivos_entrada, tension_alta_entrada, dolor_cabeza_entrada = entries

    def actualizar_registro_seleccionado():
        datos = (
            edad_entrada.get(),
            sexo_entrada.get(),
            bebidas_semana_entrada.get(),
            cervezas_semana_entrada.get(),
            bebidas_fin_semana_entrada.get(),
            bebidas_destiladas_semana_entrada.get(),
            vinos_semana_entrada.get(),
            perdidas_control_entrada.get(),
            diversion_dependencia_alcohol_entrada.get(),
            problemas_digestivos_entrada.get(),
            tension_alta_entrada.get(),
            dolor_cabeza_entrada.get()
        )
        actualizar_registro(id_entrada.get(), datos)
        actualizar_tabla()
        ventana_actualizar.destroy()

    btn_actualizar = ttk.Button(ventana_actualizar, text="Actualizar Registro", command=actualizar_registro_seleccionado)
    btn_actualizar.pack(pady=10)

# Función para eliminar un registro
def eliminar_registro_seleccionado():
    selected_item = tree.selection()[0]
    idEncuesta = tree.item(selected_item)['values'][0]
    eliminar_registro(idEncuesta)
    actualizar_tabla()

# Función para filtrar registros
def filtrar_registros():
    campo = campo_filtro.get()
    valor = valor_filtro.get()
    if not campo or not valor:
        messagebox.showerror("Error", "Debe especificar un campo y un valor para filtrar")
        return

    def filtro(registro):
        campos = {
            "idEncuesta": 0,
            "edad": 1,
            "Sexo": 2,
            "BebidasSemana": 3,
            "CervezasSemana": 4,
            "BebidasFinSemana": 5,
            "BebidasDestiladasSemana": 6,
            "VinosSemana": 7,
            "PerdidasControl": 8,
            "DiversionDependenciaAlcohol": 9,
            "ProblemasDigestivos": 10,
            "TensionAlta": 11,
            "DolorCabeza": 12
        }
        indice = campos.get(campo)
        if indice is not None:
            return str(registro[indice]) == valor
        return False

    actualizar_tabla(filtro)

# Función para exportar registros filtrados a un archivo Excel
def exportar_a_excel():
    if not registros_filtrados:
        messagebox.showerror("Error", "No hay datos para exportar")
        return

    df = pd.DataFrame(registros_filtrados, columns=["ID Encuesta", "Edad", "Sexo", "Bebidas Semana", "Cervezas Semana", "Bebidas Fin Semana", "Bebidas Destiladas Semana", "Vinos Semana", "Perdidas Control", "Diversion Dependencia Alcohol", "Problemas Digestivos", "Tension Alta", "Dolor Cabeza"])
    df.to_excel("registros_filtrados.xlsx", index=False)
    messagebox.showinfo("Éxito", "Los datos se han exportado a registros_filtrados.xlsx")

# Función para visualizar los resultados en gráficos
def visualizar_grafico():
    if not registros_filtrados:
        messagebox.showerror("Error", "No hay datos para mostrar en el gráfico")
        return

    edades = [registro[1] for registro in registros_filtrados]
    bebidas_semana = [registro[3] for registro in registros_filtrados]

    plt.bar(edades, bebidas_semana)
    plt.xlabel('Edad')
    plt.ylabel('Bebidas por Semana')
    plt.title('Consumo de Bebidas por Edad')
    plt.show()

# Función para visualizar gráficos personalizados
def visualizar_grafico_personalizado():
    if not registros_filtrados:
        messagebox.showerror("Error", "No hay datos para mostrar en el gráfico")
        return

    # Gráfico de barras
    edades = [registro[1] for registro in registros_filtrados]
    bebidas_semana = [registro[3] for registro in registros_filtrados]

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.bar(edades, bebidas_semana, color='skyblue')
    plt.xlabel('Edad')
    plt.ylabel('Bebidas por Semana')
    plt.title('Consumo de Bebidas por Edad')

    # Gráfico de pastel
    sexo = [registro[2] for registro in registros_filtrados]
    sexo_counts = {s: sexo.count(s) for s in set(sexo)}

    plt.subplot(1, 2, 2)
    plt.pie(sexo_counts.values(), labels=sexo_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Distribución por Sexo')

    plt.tight_layout()
    plt.show()

# Función para mostrar promedio por grupo de edad
def promedio_por_grupo_edad():
    if not registros_filtrados:
        messagebox.showerror("Error", "No hay datos para mostrar en el gráfico")
        return

    grupos_edad = {}
    for registro in registros_filtrados:
        edad = registro[1]
        bebidas = registro[3]
        grupo = (edad // 10) * 10  # Agrupar por décadas
        if grupo not in grupos_edad:
            grupos_edad[grupo] = []
        grupos_edad[grupo].append(bebidas)

    promedios = {grupo: np.mean(bebidas) for grupo, bebidas in grupos_edad.items()}

    plt.bar(promedios.keys(), promedios.values(), width=8, color='green')
    plt.xlabel('Grupo de Edad')
    plt.ylabel('Promedio de Bebidas por Semana')
    plt.title('Promedio de Consumo de Bebidas por Grupo de Edad')
    plt.show()

# Función para mostrar correlación entre consumo de alcohol y problemas de salud
def correlacion_consumo_problemas():
    if not registros_filtrados:
        messagebox.showerror("Error", "No hay datos para mostrar en el gráfico")
        return

    bebidas_semana = [registro[3] for registro in registros_filtrados]
    problemas_digestivos = [1 if registro[10] == 'Sí' else 0 for registro in registros_filtrados]

    plt.scatter(bebidas_semana, problemas_digestivos, color='red')
    plt.xlabel('Bebidas por Semana')
    plt.ylabel('Problemas Digestivos (1=Sí, 0=No)')
    plt.title('Correlación entre Consumo de Alcohol y Problemas Digestivos')
    plt.show()

# Crear la tabla para mostrar los registros
columns = ("idEncuesta", "edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(fill=tk.BOTH, expand=True)

# Botones para las operaciones CRUD
frame_botones = ttk.Frame(root, padding=10)
frame_botones.pack(pady=10)

btn_crear = ttk.Button(frame_botones, text="Crear", command=mostrar_ventana_crear)
btn_crear.grid(row=0, column=0, padx=5)

btn_leer = ttk.Button(frame_botones, text="Leer", command=actualizar_tabla)
btn_leer.grid(row=0, column=1, padx=5)

btn_actualizar = ttk.Button(frame_botones, text="Actualizar", command=mostrar_ventana_actualizar)
btn_actualizar.grid(row=0, column=2, padx=5)

btn_eliminar = ttk.Button(frame_botones, text="Eliminar", command=eliminar_registro_seleccionado)
btn_eliminar.grid(row=0, column=3, padx=5)

# Opciones de filtrado
frame_filtro = ttk.Frame(root, padding=10)
frame_filtro.pack(pady=10)

ttk.Label(frame_filtro, text="Campo:").grid(row=0, column=0)
campo_filtro = ttk.Entry(frame_filtro)
campo_filtro.grid(row=0, column=1, padx=5)

ttk.Label(frame_filtro, text="Valor:").grid(row=0, column=2)
valor_filtro = ttk.Entry(frame_filtro)
valor_filtro.grid(row=0, column=3, padx=5)

btn_filtrar = ttk.Button(frame_filtro, text="Aplicar Filtro", command=filtrar_registros)
btn_filtrar.grid(row=0, column=4, padx=5)

# Botón para visualizar gráficos
btn_grafico = ttk.Button(frame_filtro, text="Visualizar Gráfico", command=visualizar_grafico)
btn_grafico.grid(row=0, column=5, padx=5)

# Botón para visualizar gráficos personalizados
btn_grafico_personalizado = ttk.Button(frame_filtro, text="Gráfico Personalizado", command=visualizar_grafico_personalizado)
btn_grafico_personalizado.grid(row=0, column=6, padx=5)

# Botón para promedio por grupo de edad
btn_promedio_edad = ttk.Button(frame_filtro, text="Promedio por Grupo de Edad", command=promedio_por_grupo_edad)
btn_promedio_edad.grid(row=1, column=0, columnspan=2, pady=5)

# Botón para correlación entre consumo de alcohol y problemas de salud
btn_correlacion = ttk.Button(frame_filtro, text="Correlación Consumo-Problemas", command=correlacion_consumo_problemas)
btn_correlacion.grid(row=1, column=2, columnspan=2, pady=5)

# Botón para exportar a Excel
btn_exportar_excel = ttk.Button(frame_filtro, text="Exportar a Excel", command=exportar_a_excel)
btn_exportar_excel.grid(row=1, column=4, columnspan=2, pady=5)

# Iniciar el bucle principal de la aplicación
root.mainloop()