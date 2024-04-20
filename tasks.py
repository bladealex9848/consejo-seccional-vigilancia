from crewai import Task
from utils import load_embeddings, generar_documento, generar_pdf_solicitud, leer_puntos_desde_archivo, generar_descripcion_tarea, log_message, convert_to_utf8, generar_nombre_archivo
import os
from datetime import datetime

# Cargar los embeddings
embeddings_dir = 'embeddings'

# Verificar y crear el directorio 'embeddings' si no existe
if not os.path.exists(embeddings_dir):
    os.makedirs(embeddings_dir)
    
embeddings_dict = load_embeddings(embeddings_dir)

# Mostar los embeddings que se encuentran en el directorio 'embeddings'
print("Embeddings disponibles:")
for key in embeddings_dict.keys():
    print(f"- {key}")


# Crear el directorio 'documentos' si no existe
if not os.path.exists('documentos'):
    os.makedirs('documentos')

# Crear el directorio 'tareas' si no existe
ruta_archivo_puntos = 'puntos_solicitud.txt'
puntos = leer_puntos_desde_archivo(ruta_archivo_puntos)

if puntos:
    descripcion_tarea = generar_descripcion_tarea(puntos)
else:
    descripcion_tarea = "No se encontraron puntos de solicitud."

# Crear una tarea para la solicitud de vigilancia judicial administrativa
tarea_solicitud_vigilancia = Task(
    description=generar_descripcion_tarea(puntos),
    expected_output=(
        "Archivo .md con la solicitud de vigilancia judicial administrativa\n"
        "Archivo .pdf con la solicitud de vigilancia judicial administrativa"
    ),
    agent=None,
    human_input=False,  # Habilitar la entrada del usuario    
    # Generar un archivo de texto con la fecha y hora actual
    output_file=f"tareas/{generar_nombre_archivo('solicitud_vigilancia')}"
)

# Crear tareas para los agentes
tarea1 = Task(
    description=(
        "Se ha recibido una solicitud de vigilancia judicial administrativa. "
        "Realiza un control de legalidad sobre esta solicitud basándote en los criterios del ACUERDO No. PSAA11-8716. "
        "Evalúa la competencia territorial, legitimidad del interesado, completitud y claridad de la solicitud, y su conformidad con los procedimientos y requisitos establecidos. "
        "Presenta tu análisis en una tabla con las columnas 'Criterio', 'Descripción', 'Aplicación al Caso', y 'Observaciones', considerando si cada aspecto cumple o no con los requisitos. "
        "Verifica si la solicitud pertenece a la jurisdicción territorial de Sucre, si el solicitante tiene un interés legítimo, y si la solicitud es completa y clara.\n"
        "Posteriormente, extrae y resume la información relevante de la solicitud, incluyendo datos del solicitante (rol, identificación, dirección, contacto), detalles del proceso judicial (ubicación, tipo, número de radicado), motivos de la solicitud (incumplimientos, demoras), descripción breve de los hechos y anexos proporcionados. Presenta esta información de forma clara y concisa.\n"
        "Para terminar, genera un párrafo titulado 'Problema' que resuma la solicitud, identificando al solicitante y su rol, los detalles clave del proceso judicial, el motivo principal de la solicitud, las acciones o documentos presentados, y el estado actual o demora específica que se denuncia."
    ),
    expected_output=(
        "Tabla de control de legalidad según los criterios del ACUERDO No. PSAA11-8716\n"
        "Resumen de la información relevante de la solicitud\n"
        "Párrafo titulado 'Problema' que resuma la solicitud"
    ),
    agent=None,
    human_input=False,  # Habilitar la entrada del usuario    
    # Generar un archivo de texto con la fecha y hora actual
    output_file=f"tareas/{generar_nombre_archivo('control_legalidad')}"
)

tarea2 = Task(
    description=(
        "Analiza detalladamente la solicitud de vigilancia judicial administrativa recibida."
        "Recopila la información relevante utilizando las herramientas disponibles y elabora un proyecto de decisión."
        "Asegúrate de respetar la autonomía e independencia de los funcionarios y enfócate en verificar si la justicia se está administrando de manera oportuna y eficaz."
    ),
    expected_output='Proyecto de decisión detallado sobre la solicitud de vigilancia judicial administrativa',
    agent=None,
    # Generar un archivo de texto con la fecha y hora actual
    output_file=f"tareas/{generar_nombre_archivo('proyecto_decision')}"
)

tarea3 = Task(
    description=(
        "Revisa el proyecto de decisión elaborado por el Profesional Universitario sobre la solicitud de vigilancia judicial administrativa."
        "Realiza un análisis minucioso, verifica que se haya recopilado toda la información relevante y presenta tus observaciones y recomendaciones."
    ),
    expected_output='Observaciones y recomendaciones sobre el proyecto de decisión',
    agent=None,
    # Generar un archivo de texto con la fecha y hora actual
    output_file=f"tareas/{generar_nombre_archivo('observaciones')}"
)

tarea4 = Task(
    description=(
        "Como Magistrado del Consejo Seccional de la Judicatura, te corresponde revisar y aprobar el proyecto de decisión sobre la solicitud de vigilancia judicial administrativa."
        "Considera las observaciones y recomendaciones del Auxiliar de Magistrado y toma una decisión final, asegurándote de que se respete la autonomía e independencia de los funcionarios."
    ),
    expected_output='Decisión final aprobada sobre la solicitud de vigilancia judicial administrativa',
    agent=None,
    # Generar un archivo de texto con la fecha y hora actual
    output_file=f"tareas/{generar_nombre_archivo('decision_final')}"
)

tarea_generacion_documento = Task(
    description=(
        "Genera un documento de Word con el resumen de la solicitud de vigilancia judicial administrativa."
        "Incluye la tabla de control de legalidad, el resumen de la información relevante y el párrafo titulado 'Problema'."
        "Guarda el documento generado en la ruta especificada."
    ),
    expected_output='Documento de Word generado con el resumen de la solicitud de vigilancia judicial administrativa',
    agent=None,
    vigilancia_embedding=None,  # No acceder directamente a tarea1.result['vigilancia_embedding']     
    output_file=f"tareas/{generar_nombre_archivo('resumen_vigilancia')}"
)

# Generar una tarea en donde se le envie un correo electronico al usuario de justicia que solicito la vigilancia por parte del Consejo Seccional de la Judicatura de Sucre, y que dicha tarea sea realizada por el escribiente
tarea_envio_correo = Task(
    description=(
        "Redactar un correo electrónico y asunto para ser enviado al usuario de justicia que solicitó la vigilancia por parte del Consejo Seccional de la Judicatura de Sucre."
        "Informarle que su solicitud ha sido recibida y está siendo evaluada por el equipo correspondiente."
        "Adjuntar un resumen de la solicitud de vigilancia judicial administrativa con su respectivo estudio de legalidad."
    ),
    expected_output='Correo electrónico redactado dirigido al usuario de justicia con la confirmación de la solicitud y el resumen adjunto',
    agent=None,
    # Generar un archivo de texto con la fecha y hora actual
    output_file=f"tareas/{generar_nombre_archivo('correo_usuario_justicia')}"   
)