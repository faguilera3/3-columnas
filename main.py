import pandas as pd
import tkinter as tk
from tkinter import filedialog

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select Excel File",
        filetypes=(("Excel files", "*.xlsx"), ("all files", "*.*"))
    )
    # This line will print the selected file path to the console
    print(f"Selected file: {file_path}")
    transform_data(file_path)

def transform_data(file_path):
    # Cargar el archivo de Excel
    df = pd.read_excel(file_path)

    # Definir la cantidad de columnas por bloque
    columns_per_block = 3

    # Crear un DataFrame vacío para los datos transformados
    transformed_data = pd.DataFrame()

    # Rellenar los encabezados y mover los datos
    for i in range(len(df)):
        block_number = i + 1
        col_names = [f"Plato {block_number}", f"Precio {block_number}", f"Descripcion {block_number}"]
        transformed_data = pd.concat([transformed_data, pd.DataFrame([df.iloc[i].values], columns=col_names)], axis=1)

    # Guardar los resultados en un nuevo archivo Excel
    new_excel_path = 'mnt/data/Precios-casino-transformado.xlsx'
    transformed_data.to_excel(new_excel_path, index=False)

    # Convertir el DataFrame a un archivo delimitado por tabulaciones
    new_txt_path = 'mnt/Final/Precios-casino-transformado.txt'
    transformed_data.to_csv(new_txt_path, sep='\t', index=False, encoding='windows-1252', errors='ignore')

# Crear la ventana principal
root = tk.Tk()
root.title("Seleccionar Archivo Excel")

# Crear el botón para seleccionar el archivo
select_button = tk.Button(root, text="Seleccionar Archivo", command=select_file)
select_button.pack()

# Iniciar el bucle de eventos
root.mainloop()