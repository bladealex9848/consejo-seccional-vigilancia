import os
from agents import escribiente, profesional_universitario, auxiliar_magistrado, magistrado, usuario_justicia
from tasks import tarea_solicitud_vigilancia, tarea1, tarea2, tarea3, tarea4, tarea_envio_correo
from crewai import Crew, Process
from utils import convert_to_utf8

# Asignar los agentes a las tareas
tarea_solicitud_vigilancia.agent = usuario_justicia
tarea1.agent = escribiente
tarea2.agent = profesional_universitario
tarea3.agent = auxiliar_magistrado
tarea4.agent = magistrado
tarea_envio_correo.agent = escribiente

# Instanciar el equipo con un proceso secuencial
equipo = Crew(
    agents=[usuario_justicia, escribiente, profesional_universitario, auxiliar_magistrado, magistrado],
    tasks=[tarea_solicitud_vigilancia, tarea1, tarea2, tarea3, tarea4, tarea_envio_correo],
    verbose=2,
    process=Process.sequential
)

# ¡Poner el equipo a trabajar!
resultado = equipo.kickoff()
print("######################")
print(resultado)

# Cambiar la codificación de los archivos .md a utf-8
directorio_md = 'tareas'

# Obtener la lista de archivos .md en el directorio
archivos_md = [archivo for archivo in os.listdir(directorio_md) if archivo.endswith('.md')]

# Cambiar la codificación de cada archivo .md a utf-8
for archivo_md in archivos_md:
    ruta_archivo = os.path.join(directorio_md, archivo_md)
    convert_to_utf8(ruta_archivo)