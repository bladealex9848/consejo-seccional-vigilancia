from crewai import Agent
from crewai_tools import SerperDevTool, JSONSearchTool, PDFSearchTool
from utils import load_embedding
import os

# Herramientas para trabajar con archivos JSON específicos
# formato_vigilancia_tool = JSONSearchTool(json_path='embeddings/formato_vigilancia.json')
# instructivo_vigilancia_judicial_administrativa_tool = JSONSearchTool(json_path='embeddings/instructivo_vigilancia_judicial_administrativa.json')
#acuerdo_PSAA11_8716_ley_270_1996_tool = JSONSearchTool(json_path='embeddings/acuerdo_PSAA11_8716_ley_270_1996.json')

# Herramientas para trabajar con archivos PDF específicos
formato_vigilancia_pdf_tool = PDFSearchTool(pdf='documentos/formato_vigilancia.pdf')
instructivo_vigilancia_judicial_administrativa_pdf_tool = PDFSearchTool(pdf='documentos/instructivo_vigilancia_judicial_administrativa.pdf')
acuerdo_PSAA11_8716_ley_270_1996_pdf_tool = PDFSearchTool(pdf='documentos/acuerdo_PSAA11_8716_ley_270_1996.pdf')

# Definir las rutas de los archivos
ruta_escribiente_embedding = 'perfiles/escribiente_embedding.json'
ruta_profesional_universitario_embedding = 'perfiles/profesional_universitario_embedding.json'
ruta_auxiliar_magistrado_embedding = 'perfiles/auxiliar_magistrado_embedding.json'
ruta_magistrado_embedding = 'perfiles/magistrado_embedding.json'
ruta_usuario_justicia_embedding = 'perfiles/usuario_justicia_embedding.json'
ruta_puntos_solicitud = 'puntos_solicitud.txt'

# Validar las rutas de los archivos
if not os.path.exists(ruta_escribiente_embedding):
    raise FileNotFoundError(f"El archivo {ruta_escribiente_embedding} no existe.")

if not os.path.exists(ruta_profesional_universitario_embedding):
    raise FileNotFoundError(f"El archivo {ruta_profesional_universitario_embedding} no existe.")

if not os.path.exists(ruta_auxiliar_magistrado_embedding):
    raise FileNotFoundError(f"El archivo {ruta_auxiliar_magistrado_embedding} no existe.")

if not os.path.exists(ruta_magistrado_embedding):
    raise FileNotFoundError(f"El archivo {ruta_magistrado_embedding} no existe.")

if not os.path.exists(ruta_usuario_justicia_embedding):
    raise FileNotFoundError(f"El archivo {ruta_usuario_justicia_embedding} no existe.")

if not os.path.exists(ruta_puntos_solicitud):
    raise FileNotFoundError(f"El archivo {ruta_puntos_solicitud} no existe.")

# Cargar las herramientas
search_tool = SerperDevTool()

# Definir los agentes con roles, objetivos, herramientas, atributos adicionales y embeddings de perfil
escribiente = Agent(
    role='Escribiente',
    goal='Recibir y realizar el control de legalidad de las solicitudes de vigilancia judicial administrativa',
    backstory=(
        "Eres un Escribiente del Consejo Seccional de la Judicatura de Sucre."
        "Tu función es recepcionar las solicitudes de vigilancia judicial administrativa y realizar un control de legalidad sobre ellas."
        "Debes evaluar cada solicitud según los criterios del ACUERDO No. PSAA11-8716 y presentar un análisis detallado."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[acuerdo_PSAA11_8716_ley_270_1996_pdf_tool, formato_vigilancia_pdf_tool, instructivo_vigilancia_judicial_administrativa_pdf_tool, search_tool],
    max_rpm=100,
    profile_embedding=load_embedding('perfiles/escribiente_embedding.json') or {}  # Asignar un diccionario vacío si el archivo no existe
)

profesional_universitario = Agent(
    role='Profesional Universitario',
    goal='Sustanciar las vigilancias judiciales administrativas',
    backstory=(
        "Eres un Profesional Universitario experto en sustanciar vigilancias judiciales administrativas en el Consejo Seccional de la Judicatura."
        "Tu tarea es analizar detalladamente cada solicitud de vigilancia, recopilar la información necesaria y elaborar los proyectos de decisión."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[acuerdo_PSAA11_8716_ley_270_1996_pdf_tool, formato_vigilancia_pdf_tool, instructivo_vigilancia_judicial_administrativa_pdf_tool, search_tool],
    profile_embedding=load_embedding('perfiles/profesional_universitario_embedding.json')
)

auxiliar_magistrado = Agent(
    role='Auxiliar de Magistrado',
    goal='Asistir al Magistrado en la revisión de las vigilancias judiciales administrativas',
    backstory=(
        "Eres un Auxiliar de Magistrado del Consejo Seccional de la Judicatura."
        "Tu función es apoyar al Magistrado en la revisión de las vigilancias judiciales administrativas."
        "Debes realizar un análisis detallado de cada caso y presentar tus observaciones al Magistrado."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[acuerdo_PSAA11_8716_ley_270_1996_pdf_tool, formato_vigilancia_pdf_tool, instructivo_vigilancia_judicial_administrativa_pdf_tool, search_tool],
    cache=False,
    profile_embedding=load_embedding('perfiles/auxiliar_magistrado_embedding.json')
)

magistrado = Agent(
    role='Magistrado del Consejo Seccional de la Judicatura',
    goal='Revisar y aprobar las vigilancias judiciales administrativas',
    backstory=(
        "Eres un Magistrado del Consejo Seccional de la Judicatura con amplia experiencia en la revisión y aprobación de vigilancias judiciales administrativas."
        "Tu objetivo es garantizar que las vigilancias se realicen de manera oportuna, eficaz y respetando la autonomía e independencia de los funcionarios."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[acuerdo_PSAA11_8716_ley_270_1996_pdf_tool, formato_vigilancia_pdf_tool, instructivo_vigilancia_judicial_administrativa_pdf_tool, search_tool],
    max_rpm=100,
    profile_embedding=load_embedding('perfiles/magistrado_embedding.json')
)

usuario_justicia = Agent(
    role='Usuario de Justicia',
    goal='Crear correctamente una solicitud de vigilancia judicial administrativa',
    backstory=(
        "Eres un usuario de justicia que busca presentar una solicitud de vigilancia judicial administrativa."
        "Tienes conocimiento de los criterios establecidos en el ACUERDO No. PSAA11-8716 y la LEY 270 DE 1996."
        "Sabes cómo completar el FORMATO DE VIGILANCIA y proporcionar la información necesaria para una solicitud válida."
    ),
    verbose=True,
    allow_delegation=True,
    tools=[acuerdo_PSAA11_8716_ley_270_1996_pdf_tool, formato_vigilancia_pdf_tool, instructivo_vigilancia_judicial_administrativa_pdf_tool, search_tool],
    max_rpm=100,
    profile_embedding=load_embedding('perfiles/usuario_justicia_embedding.json')
)