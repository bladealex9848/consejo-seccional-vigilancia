# Vigilancia Judicial Administrativa

## Tabla de Contenidos
1. [Descripción](#descripción)
2. [Características Principales](#características-principales)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Requisitos Previos](#requisitos-previos)
5. [Instalación](#instalación)
6. [Configuración](#configuración)
7. [Uso](#uso)
8. [Manual Técnico](#manual-técnico)
9. [Manual de Usuario](#manual-de-usuario)
10. [Contribución](#contribución)
11. [Registro de Cambios](#registro-de-cambios)
12. [Créditos](#créditos)
13. [Licencia](#licencia)

## Descripción

El proyecto de Vigilancia Judicial Administrativa es un sistema avanzado desarrollado para automatizar y mejorar los procesos de vigilancia judicial en los Consejos Seccionales de la Judicatura de Colombia. Utilizando tecnologías de inteligencia artificial y procesamiento de lenguaje natural, esta herramienta permite analizar solicitudes de vigilancia, realizar controles de legalidad y generar proyectos de decisión de manera eficiente y precisa.

Este sistema responde a la necesidad de optimizar los flujos de trabajo administrativos en el sector judicial, reduciendo tiempos de procesamiento y asegurando la consistencia en la aplicación de criterios legales, particularmente los establecidos en el ACUERDO No. PSAA11-8716.

## Características Principales

- **Análisis Automatizado de Solicitudes**: 
  - Procesamiento y evaluación automática de solicitudes de vigilancia judicial.
  - Identificación de elementos clave y requisitos legales en documentos.

- **Control de Legalidad Inteligente**: 
  - Verificación basada en los criterios establecidos en el ACUERDO No. PSAA11-8716.
  - Validación automática de competencia y procedencia de la vigilancia.

- **Procesamiento Avanzado de Documentos**:
  - Generación de embeddings a partir de documentos PDF para análisis detallado.
  - Extracción inteligente de información relevante de documentos judiciales.

- **Sistema de Roles Diferenciados**:
  - Funcionalidades específicas para cada rol dentro del flujo de trabajo:
    - Solicitante
    - Escribiente
    - Profesional Universitario
    - Auxiliar de Consejero
    - Consejero

- **Generación Automática de Documentos**:
  - Creación de proyectos de decisión en formato Markdown.
  - Producción de resúmenes y análisis de casos.

- **Análisis de Precedentes**:
  - Búsqueda y análisis de casos similares para apoyar la toma de decisiones.

- **Interfaz Intuitiva**:
  - Diseño centrado en el usuario para facilitar la operación del sistema.
  - Flujos de trabajo optimizados para cada etapa del proceso.

## Estructura del Proyecto

```
vigilancia-judicial/
│
├── embeddings/                # Directorio de almacenamiento de embeddings
│
├── generador_embeddings/      # Módulo para procesamiento de documentos
│   ├── generador_embeddings.py # Generación de embeddings de documentos
│   └── generador_perfiles.py  # Generación de perfiles basados en embeddings
│
├── perfiles/                  # Almacenamiento de perfiles de embeddings
│   ├── auxiliar_magistrado_embedding.json   # Perfil para auxiliar de magistrado
│   ├── escribiente_embedding.json           # Perfil para escribiente
│   ├── magistrado_embedding.json            # Perfil para magistrado
│   ├── profesional_universitario_embedding.json  # Perfil para profesional universitario
│   └── usuario_justicia_embedding.json      # Perfil para usuario de justicia
│
├── tareas/                    # Directorio de tareas programadas
│
├── .gitignore                 # Archivo de configuración git
├── LICENSE                    # Archivo de licencia
├── README.md                  # Documentación del proyecto (este archivo)
├── agents.py                  # Implementación de agentes inteligentes
├── converter.py               # Utilidades de conversión de formatos
├── log.json                   # Archivo de registro de actividades
├── main.py                    # Punto de entrada principal de la aplicación
├── puntos_solicitud.txt       # Archivo de configuración de puntos de solicitud
├── requirements.txt           # Dependencias del proyecto
├── tasks.py                   # Definición de tareas automatizadas
└── utils.py                   # Funciones de utilidad general
```

## Requisitos Previos

- Python 3.7 o superior
- Acceso a internet para descargar modelos de lenguaje y dependencias
- Permisos de lectura/escritura en el sistema de archivos local
- Memoria RAM mínima recomendada: 8GB

## Instalación

1. Clone el repositorio:
   ```bash
   git clone https://github.com/bladealex9848/consejo-seccional-vigilancia.git
   ```

2. Navegue al directorio del proyecto:
   ```bash
   cd consejo-seccional-vigilancia
   ```

3. Instale las dependencias requeridas:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure el entorno (opcional):
   ```bash
   python setup.py
   ```

## Configuración

1. Modifique el archivo `config.yaml` con los parámetros específicos de su entorno:
   ```yaml
   sistema:
     modo_debug: false
     directorio_documentos: "./documentos/"
     directorio_salida: "./documentos/decisiones/"
   
   modelos:
     embedding: "sentence-transformers/all-MiniLM-L6-v2"
     analisis_texto: "gpt-4"
   
   parametros:
     umbral_similitud: 0.85
     max_tokens: 2048
   ```

2. Asegúrese de que los directorios especificados en la configuración existan y tengan los permisos adecuados.

## Uso

1. Coloque los documentos PDF de solicitudes de vigilancia en el directorio `documentos/solicitudes/`.

2. Ejecute el generador de embeddings para procesar los documentos:
   ```bash
   python generador_embeddings/generador_embeddings.py
   ```

3. Inicie el sistema principal:
   ```bash
   python consejo_seccional/main.py
   ```

4. Siga las instrucciones en pantalla para completar el flujo de trabajo según su rol en el sistema.

### Ejemplo de Flujo de Trabajo:

1. **Profesional Universitario**:
   - Cargue una nueva solicitud de vigilancia
   - Realice el control inicial de legalidad
   - Asigne la solicitud a un Auxiliar de Consejero

2. **Auxiliar de Consejero**:
   - Revise el control de legalidad
   - Genere un proyecto de decisión
   - Envíe para revisión del Consejero

3. **Consejero**:
   - Revise el proyecto de decisión
   - Apruebe o solicite modificaciones
   - Finalice el proceso de vigilancia

## Manual Técnico

### Arquitectura del Sistema

El sistema de Vigilancia Judicial Administrativa está construido con una arquitectura modular centrada en el procesamiento de lenguaje natural y la automatización de decisiones. Los componentes principales son:

1. **Módulo de Procesamiento de Documentos**:
   - Utiliza la biblioteca PyPDF2 para extraer texto de documentos PDF.
   - Implementa sentence_transformers para generar embeddings vectoriales de los documentos.
   - Almacena los embeddings para su posterior análisis y comparación.

2. **Módulo de Control de Legalidad**:
   - Aplica reglas basadas en el ACUERDO No. PSAA11-8716.
   - Verifica automáticamente la competencia y procedencia de la vigilancia.
   - Genera informes de control de legalidad con recomendaciones.

3. **Módulo de Generación de Decisiones**:
   - Utiliza modelos de lenguaje para generar proyectos de decisión.
   - Implementa plantillas predefinidas para mantener la estructura legal adecuada.
   - Incorpora información contextual y argumentos legales relevantes.

4. **Sistema de Gestión de Flujo de Trabajo**:
   - Coordina las actividades entre los diferentes roles.
   - Mantiene registros de estado y trazabilidad de cada solicitud.
   - Implementa notificaciones y alertas para eventos críticos.

### Flujo de Datos

```
Documento PDF → Extracción de Texto → Generación de Embeddings → Análisis de Contenido
                                                                 ↓
Proyecto de Decisión ← Generación de Documento ← Control de Legalidad
```

### Consideraciones de Seguridad

- Los documentos y datos son procesados localmente, sin enviar información sensible a servicios externos.
- Se implementa un sistema de autenticación para controlar el acceso según los roles definidos.
- La información sensible se maneja siguiendo las normativas de protección de datos aplicables.

### Optimización y Rendimiento

- Los modelos de embeddings se cargan en memoria para un procesamiento más rápido.
- La generación de documentos utiliza plantillas pre-compiladas para mejorar la eficiencia.
- Se implementa un sistema de caché para minimizar el reprocesamiento de documentos ya analizados.

## Manual de Usuario

### Inicio de Sesión

1. Ejecute la aplicación siguiendo las instrucciones en la sección [Uso](#uso).
2. Inicie sesión con sus credenciales asociadas a su rol en el sistema.

### Interfaz Principal

La interfaz se adapta al rol del usuario, mostrando únicamente las funciones relevantes:

- **Panel de Navegación**: Permite acceder a las diferentes secciones del sistema.
- **Bandeja de Solicitudes**: Muestra las solicitudes pendientes y su estado actual.
- **Área de Trabajo**: Espacio principal para revisar y procesar documentos.
- **Panel de Notificaciones**: Alertas sobre nuevas asignaciones o cambios de estado.

### Guía por Roles

#### Para Escribientes:

1. **Recepción de Solicitudes**:
   - Seleccione "Nueva Solicitud" en el panel principal.
   - Cargue el documento PDF de la solicitud.
   - Complete los metadatos básicos (fecha, solicitante, despacho judicial).

2. **Asignación Inicial**:
   - Verifique que la información esté completa.
   - Asigne la solicitud al Profesional Universitario correspondiente.

#### Para Profesionales Universitarios:

1. **Control de Legalidad**:
   - Acceda a la solicitud desde su bandeja de entrada.
   - Revise el documento y la información extraída automáticamente.
   - Valide o modifique el control de legalidad generado por el sistema.

2. **Proceso de Asignación**:
   - Determine el Magistrado competente.
   - Asigne la solicitud al Auxiliar del Consejero correspondiente.

#### Para Auxiliares de Consejero:

1. **Revisión de Control de Legalidad**:
   - Acceda a la solicitud asignada.
   - Verifique el control de legalidad realizado.
   - Solicite correcciones si es necesario.

2. **Generación de Proyecto de Decisión**:
   - Seleccione "Generar Proyecto de Decisión".
   - Revise el proyecto generado automáticamente.
   - Edite según sea necesario.
   - Envíe para aprobación del Consejero.

#### Para Magistrados:

1. **Revisión Final**:
   - Acceda a los proyectos pendientes de revisión.
   - Analice el contenido y fundamentación jurídica.
   - Apruebe o solicite modificaciones.

2. **Finalización del Proceso**:
   - Apruebe el proyecto final.
   - Genere la decisión oficial en el formato requerido.

### Solución de Problemas Comunes

1. **Documentos no reconocidos correctamente**:
   - Verifique que el PDF no esté protegido o sea un escaneo de imagen.
   - Utilice la función "Extracción Manual" para ingresar la información clave.

2. **Control de legalidad incorrecto**:
   - Revise los criterios específicos que no se identificaron correctamente.
   - Utilice la opción "Editar Control" para ajustar manualmente.

3. **Proyecto de decisión incompleto**:
   - Verifique que todos los campos requeridos estén completos.
   - Utilice las plantillas alternativas disponibles en la sección "Herramientas".

## Contribución

Las contribuciones son bienvenidas y apreciadas. Para contribuir a este proyecto:

1. Fork el repositorio
2. Cree una rama para su nueva función (`git checkout -b feature/nueva-funcion`)
3. Realice sus cambios y documente adecuadamente
4. Ejecute las pruebas para asegurar que todo funciona correctamente
5. Haga commit de sus cambios (`git commit -m "Agrega nueva función: descripción"`)
6. Push a la rama (`git push origin feature/nueva-funcion`)
7. Abra un Pull Request

### Pautas de Contribución

- Siga las convenciones de codificación establecidas en el proyecto.
- Incluya pruebas para nuevas funcionalidades.
- Actualice la documentación según sea necesario.
- Asegúrese de que su código pase todas las pruebas existentes.

## Registro de Cambios

### [1.0.0] - 2025-03-29
- Lanzamiento inicial del sistema de Vigilancia Judicial Administrativa
- Implementación completa del flujo de trabajo básico
- Soporte para análisis de documentos PDF
- Generación automática de proyectos de decisión

### [0.9.0] - 2025-03-15
- Versión beta con todas las funcionalidades principales
- Mejoras en la interfaz de usuario
- Optimización del rendimiento en la generación de embeddings

### [0.8.0] - 2025-03-01
- Implementación del sistema de roles y permisos
- Integración del módulo de control de legalidad
- Mejoras en el procesamiento de documentos

### [0.7.0] - 2025-02-15
- Primera versión alfa con funcionalidades básicas
- Desarrollo del generador de embeddings
- Implementación inicial de la interfaz de usuario

## Créditos

Desarrollado y mantenido por Alexander Oviedo Fadul, Profesional Universitario Grado 11 en el Consejo Seccional de la Judicatura de Sucre.

[GitHub](https://github.com/bladealex9848) | [Website](https://alexanderoviedofadul.dev/) | [Instagram](https://www.instagram.com/alexander.oviedo.fadul) | [Twitter](https://twitter.com/alexanderofadul) | [Facebook](https://www.facebook.com/alexanderof/) | [WhatsApp](https://api.whatsapp.com/send?phone=573015930519&text=Hola%20!Quiero%20conversar%20contigo!) | [LinkedIn](https://www.linkedin.com/in/alexander-oviedo-fadul/)

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - vea el archivo [MIT License](https://opensource.org/licenses/MIT) para más detalles.
