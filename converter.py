import os
import pypandoc
from utils import log_message

def convertir_md_a_pdf(directorio_md, directorio_pdf):
    # Crear el directorio de salida si no existe
    os.makedirs(directorio_pdf, exist_ok=True)

    # Obtener la lista de archivos .md en el directorio de origen
    archivos_md = [archivo for archivo in os.listdir(directorio_md) if archivo.endswith('.md')]

    for archivo_md in archivos_md:
        ruta_md = os.path.join(directorio_md, archivo_md)
        nombre_pdf = os.path.splitext(archivo_md)[0] + '.pdf'
        ruta_pdf = os.path.join(directorio_pdf, nombre_pdf)

        # Verificar si el archivo PDF ya existe en el directorio de destino
        if not os.path.exists(ruta_pdf):
            # Convertir el archivo .md a PDF utilizando pypandoc con xelatex como motor de PDF
            pypandoc.convert_file(ruta_md, 'pdf', outputfile=ruta_pdf, extra_args=['--pdf-engine=pdflatex'])
            log_message(f"Archivo {archivo_md} convertido a PDF: {nombre_pdf}", "convertir_md_a_pdf")
        else:
            log_message(f"El archivo PDF {nombre_pdf} ya existe en el directorio de destino", "convertir_md_a_pdf")

# Convertir los archivos .md a PDF
directorio_md = 'tareas'
directorio_pdf = 'tareas/pdf'
convertir_md_a_pdf(directorio_md, directorio_pdf)