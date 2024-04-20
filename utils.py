import os
import json
from datetime import datetime
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
import pypandoc
import codecs

def convert_to_utf8(filename):
    with codecs.open(filename, 'r', encoding='latin1') as file:
        content = file.read()

    with codecs.open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def log_message(message, function_name):
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "function": function_name,
        "message": message
    }
    
    log_file_path = "log.json"
    
    # Verificar si el archivo log.json existe, y crearlo si no existe
    if not os.path.exists(log_file_path):
        with open(log_file_path, "w") as log_file:
            log_file.write("[]")
    
    # Leer el contenido existente del archivo log.json
    with open(log_file_path, "r") as log_file:
        log_data = json.load(log_file)
    
    # Agregar la nueva entrada de registro al final de los datos existentes
    log_data.append(log_entry)
    
    # Escribir los datos actualizados en el archivo log.json
    with open(log_file_path, "w") as log_file:
        json.dump(log_data, log_file, indent=2)

def load_embedding(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            embedding = json.load(file)
        return embedding
    else:
        print(f"El archivo {file_path} no existe.")
        return None  # Retornar None si el archivo no existe

def load_embeddings(embeddings_dir):
    # Convertir la ruta relativa a una ruta absoluta
    absolute_embeddings_dir = os.path.abspath(embeddings_dir)
    
    # Crear el directorio si no existe
    if not os.path.exists(absolute_embeddings_dir):
        print(f"Creando el directorio {absolute_embeddings_dir}...")
        os.makedirs(absolute_embeddings_dir, exist_ok=True)

    embeddings = {}
    for filename in os.listdir(absolute_embeddings_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(absolute_embeddings_dir, filename)
            with open(file_path, 'r') as file:
                embedding = json.load(file)
                document_id = os.path.splitext(filename)[0]
                embeddings[document_id] = embedding
    return embeddings

def generar_documento(contenido, ruta_archivo):
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
        
        if os.path.exists(ruta_archivo):
            log_message(f"Documento generado exitosamente en: {ruta_archivo}", "generar_documento")
        else:
            log_message(f"El documento no se encontró en la ruta especificada: {ruta_archivo}", "generar_documento")
    except Exception as e:
        log_message(f"Error al generar el documento: {e}", "generar_documento")

def generar_pdf_solicitud(datos_solicitud, ruta_pdf):
    try:
        c = canvas.Canvas(ruta_pdf, pagesize=letter)
        styles = getSampleStyleSheet()
    
        # Agregar título
        titulo = "Solicitud de Vigilancia Judicial Administrativa"
        p = Paragraph(titulo, styles['Heading1'])
        p.wrapOn(c, 500, 50)
        p.drawOn(c, 50, 750)
        
        # Agregar datos del solicitante
        solicitante = f"Nombre: {datos_solicitud['nombre']}\nIdentificación: {datos_solicitud['identificacion']}\nDirección: {datos_solicitud['direccion']}\nDatos de contacto: {datos_solicitud['contacto']}"
        p = Paragraph(solicitante, styles['Normal'])
        p.wrapOn(c, 500, 100)
        p.drawOn(c, 50, 650)
        
        # Agregar detalles del proceso
        proceso = f"Despacho: {datos_solicitud['despacho']}\nTipo de proceso: {datos_solicitud['tipo_proceso']}\nNúmero de radicado: {datos_solicitud['radicado']}"
        p = Paragraph(proceso, styles['Normal'])
        p.wrapOn(c, 500, 100)
        p.drawOn(c, 50, 550)
        
        # Agregar motivo de la solicitud
        motivo = f"Motivo de la solicitud: {datos_solicitud['motivo']}"
        p = Paragraph(motivo, styles['Normal'])
        p.wrapOn(c, 500, 50)
        p.drawOn(c, 50, 450)
        
        # Agregar descripción de los hechos
        hechos = f"Descripción de los hechos: {datos_solicitud['hechos']}"
        p = Paragraph(hechos, styles['Normal'])
        p.wrapOn(c, 500, 100)
        p.drawOn(c, 50, 350)
        
        # Agregar anexos
        anexos = f"Anexos: {datos_solicitud['anexos']}"
        p = Paragraph(anexos, styles['Normal'])
        p.wrapOn(c, 500, 50)
        p.drawOn(c, 50, 250)
        
        c.showPage()
        c.save()
        
        if os.path.exists(ruta_pdf):
            log_message(f"PDF generado exitosamente en: {ruta_pdf}", "generar_pdf_solicitud")
        else:
            log_message(f"El PDF no se encontró en la ruta especificada: {ruta_pdf}", "generar_pdf_solicitud")
    except Exception as e:
        log_message(f"Error al generar el PDF: {e}", "generar_pdf_solicitud")

def generar_descripcion_tarea(puntos):
    descripcion = (
        "Como usuario de justicia, deseas presentar una solicitud de vigilancia judicial administrativa.\n"
        "Responde las siguientes preguntas para proporcionar la información necesaria para la solicitud:\n"
    )
    descripcion += puntos
    descripcion += (
        "Con base en tus respuestas, se generará un archivo .md y un archivo .pdf con la solicitud de vigilancia judicial administrativa."
    )
    return descripcion

def leer_puntos_desde_archivo(ruta_archivo):
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    else:
        print(f"El archivo {ruta_archivo} no existe.")
        return ""  # Retornar una cadena vacía si el archivo no existe
    
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
            # Convertir el archivo .md a PDF utilizando pypandoc
            pypandoc.convert_file(ruta_md, 'pdf', outputfile=ruta_pdf)
            log_message(f"Archivo {archivo_md} convertido a PDF: {nombre_pdf}", "convertir_md_a_pdf")
        else:
            log_message(f"El archivo PDF {nombre_pdf} ya existe en el directorio de destino", "convertir_md_a_pdf")

def generar_nombre_archivo(prefijo):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"{prefijo}_{timestamp}.md"
    return nombre_archivo