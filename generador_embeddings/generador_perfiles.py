from sentence_transformers import SentenceTransformer
import PyPDF2
import json
import os

# Cargar el modelo pre-entrenado de Sentence Transformers
model = SentenceTransformer('all-MiniLM-L6-v2')

# Definir los perfiles de los roles
perfiles = {
    'usuario_justicia': "El usuario de justicia es la persona que busca presentar una solicitud de vigilancia judicial administrativa. Tiene conocimiento de los criterios establecidos en el ACUERDO No. PSAA11-8716 y la LEY 270 DE 1996. Sabe cómo completar el FORMATO DE VIGILANCIA y proporcionar la información necesaria para una solicitud válida.",
    'escribiente': "El escribiente es el encargado de recibir las solicitudes de vigilancia judicial administrativa y realizar un control de legalidad sobre ellas. Debe evaluar cada solicitud según los criterios del ACUERDO No. PSAA11-8716 y presentar un análisis detallado.",
    'profesional_universitario': "El profesional universitario es un experto en sustanciar vigilancias judiciales administrativas en el Consejo Seccional de la Judicatura. Su tarea es analizar detalladamente cada solicitud de vigilancia, recopilar la información necesaria y elaborar los proyectos de decisión.",
    'auxiliar_magistrado': "El auxiliar de magistrado apoya al magistrado en la revisión de las vigilancias judiciales administrativas. Debe realizar un análisis detallado de cada caso y presentar sus observaciones al magistrado.",
    'magistrado': "El magistrado del Consejo Seccional de la Judicatura tiene amplia experiencia en la revisión y aprobación de vigilancias judiciales administrativas. Su objetivo es garantizar que las vigilancias se realicen de manera oportuna, eficaz y respetando la autonomía e independencia de los funcionarios."
}

# Definir los documentos PDF adicionales con rutas seguras
documentos_pdf = [
    os.path.join("documentos", "ACUERDO No. PSAA11-8716 - LEY 270 DE 1996.pdf"),
    os.path.join("documentos", "instructivo Vigilancia Judicial Administrativa.pdf"),
    os.path.join("documentos", "FORMATO VIGILANCIA.pdf")
]

# Función para extraer texto de un archivo PDF
def extract_text_from_pdf(pdf_path):
    try:
        # Construir la ruta completa de forma segura
        full_pdf_path = os.path.join(os.getcwd(), pdf_path)
        
        with open(full_pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
        return text
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo PDF {full_pdf_path}")
        return ""


# Generar embeddings de los perfiles y documentos PDF
def generate_embeddings(text):
    embedding = model.encode(text)
    return embedding.tolist()

# Guardar los embeddings en un archivo JSON
def save_embeddings(profile_name, embeddings, output_folder):
    output_file = os.path.join(output_folder, f"{profile_name}_embedding.json")
    with open(output_file, 'w') as file:
        json.dump(embeddings, file)

# Generar y guardar los embeddings de los perfiles y documentos PDF
output_folder = '../consejo_seccional/perfiles'

for profile_name, profile_text in perfiles.items():
    # Generar embeddings del perfil específico
    profile_embeddings = generate_embeddings(profile_text)
    
    # Generar embeddings de los documentos PDF adicionales
    pdf_embeddings = []
    for pdf_file in documentos_pdf:
        pdf_path = os.path.join('', pdf_file)
        pdf_text = extract_text_from_pdf(pdf_path)
        if pdf_text:
            pdf_embedding = generate_embeddings(pdf_text)
            pdf_embeddings.append(pdf_embedding)
    
    # Combinar los embeddings del perfil y los documentos PDF
    combined_embeddings = profile_embeddings + pdf_embeddings
    
    # Guardar los embeddings combinados en un archivo JSON
    save_embeddings(profile_name, combined_embeddings, output_folder)