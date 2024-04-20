# Consejo Seccional de la Judicatura - Vigilancia Judicial Administrativa

Este proyecto tiene como objetivo automatizar y mejorar el proceso de vigilancia judicial administrativa en el Consejo Seccional de la Judicatura de Sucre, Colombia. Utilizando técnicas de inteligencia artificial y procesamiento de lenguaje natural, el sistema es capaz de analizar solicitudes de vigilancia, realizar un control de legalidad y generar proyectos de decisión de manera eficiente.

## Características principales

- **Análisis Automatizado**: Evaluación y procesamiento automático de solicitudes de vigilancia judicial administrativa.
- **Control de Legalidad**: Verificación basada en los criterios del ACUERDO No. PSAA11-8716.
- **Generación de Embeddings**: Creación de embeddings a partir de documentos PDF para análisis detallado.
- **Gestión de Roles**: Funcionalidades asignadas a diferentes roles como Escribiente, Profesional Universitario, Auxiliar de Magistrado y Magistrado.
- **Generación de Documentos**: Producción automática de documentos en formato Word con resúmenes y proyectos de decisión.

## Requisitos Técnicos

- **Python 3.7 o superior**
- Bibliotecas necesarias incluidas en `requirements.txt`.

| Biblioteca             | Descripción                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------------ |
| crewai                 | Biblioteca de IA para análisis de texto y generación de embeddings.                              |
| sentence_transformers  | Herramienta para transformaciones avanzadas de texto en vectores.                                |
| PyPDF2                 | Biblioteca para manipular archivos PDF en Python.                                                |
| python-docx            | Creación y modificación de documentos Word usando Python.                                        |

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/bladealex9848/consejo-seccional-vigilancia.git
   ```
2. Accede al directorio del proyecto y instala las dependencias:
   ```bash
   cd consejo-seccional-vigilancia
   pip install -r requirements.txt
   ```

## Uso

1. Coloca los documentos PDF de las solicitudes de vigilancia en la carpeta `documentos/`.
2. Ejecuta el script `generador_embeddings.py` para procesar los documentos:
   ```bash
   python generador_embeddings/generador_embeddings.py
   ```
3. Inicia el proceso de vigilancia judicial administrativa:
   ```bash
   python consejo_seccional/main.py
   ```

## Contribución

Para contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu nueva función o corrección (`git checkout -b mi-nueva-funcion`).
3. Realiza tus cambios y haz commit (`git commit -m "Agregar nueva función"`).
4. Envía tus cambios (`git push origin mi-nueva-funcion`).
5. Abre una Pull Request en GitHub.

## Licencia

Este proyecto está distribuido bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Autor

<p>Este código fue creado por <strong>Alexander Oviedo Fadul</strong> como ejemplo de una Inteligencia Artificial entrenable. Si tiene alguna pregunta o sugerencia, no dude en contactar al autor a través de GitHub o enviando un correo electrónico a alexander.oviedo.fadul@gmail.com.</p>

## Contribuciones

<p>Este código es un ejemplo y está disponible para que cualquiera pueda utilizarlo y modificarlo. Si desea contribuir con mejoras o correcciones, puede enviar una solicitud de pull a través de GitHub. Todas las contribuciones serán revisadas y, si se aprueban, serán incorporadas al repositorio.</p>

## Agradecimientos

<p><strong>Agradezco a Dios, a mi familia y amigos</strong>. Sin su ayuda, esta aplicación no habría sido posible.</p>

## Donaciones

Somos un equipo dedicado al desarrollo de soluciones de software en el ámbito judicial, con un enfoque especial en la automatización y mejora de los procesos de vigilancia judicial administrativa. Nuestro sistema utiliza técnicas avanzadas de inteligencia artificial para analizar solicitudes de vigilancia, asegurar el cumplimiento de los estándares legales y optimizar la toma de decisiones judiciales.

A lo largo de su implementación, hemos observado la significativa eficiencia y valor que nuestro sistema ha aportado a los operadores judiciales y partes interesadas, permitiéndoles gestionar los procesos con mayor precisión y en menor tiempo. Sin embargo, para continuar con el desarrollo y mejora de este proyecto innovador, necesitamos apoyo económico.

Tu contribución nos permitirá mantener y mejorar nuestro sistema, asegurando que siga siendo una herramienta efectiva y actualizada para la gestión judicial. Cada donación, no importa su tamaño, es crucial para nosotros y nos ayuda a continuar ofreciendo y mejorando este servicio indispensable.

Agradecemos de antemano tu apoyo y esperamos que nuestro sistema de vigilancia judicial administrativa siga siendo una herramienta valiosa en tu labor diaria.

Gracias por tu tiempo y consideración.


### Métodos:

<ul>
<li><a href="https://www.paypal.com/donate/?hosted_button_id=AVZSDFALB7QJQ" target="_blank">Pypal</a></li>
</ul>

<p><strong>Recuerda que tu imaginación es tu única frontera.</strong></p>