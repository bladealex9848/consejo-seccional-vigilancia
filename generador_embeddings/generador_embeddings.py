from sentence_transformers import SentenceTransformer
import PyPDF2
import json
import os

# Cargar el modelo pre-entrenado de Sentence Transformers
print("Cargando el modelo pre-entrenado...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Función para extraer texto de un archivo PDF
def extract_text_from_pdf(pdf_path):
    print(f"Extrayendo texto de: {pdf_path}")
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or " "  # Asegurar que se añade un espacio si extract_text retorna None
    return text

# Generar embeddings de un documento PDF
def generate_embeddings(pdf_path):
    print(f"Generando embeddings para: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)
    paragraphs = [p for p in text.split('\n\n') if p.strip()]  # Eliminar párrafos vacíos
    doc_embeddings = model.encode(paragraphs)
    return doc_embeddings.tolist()

# Guardar los embeddings en un archivo JSON
def save_embeddings(embeddings, output_file):
    output_folder = os.path.dirname(output_file)

    if not os.path.exists(output_folder):
        print(f"Creando carpeta para embeddings: {output_folder}")
        os.makedirs(output_folder, exist_ok=True)

    print(f"Guardando embeddings en: {output_file}")
    with open(output_file, 'w') as file:
        json.dump(embeddings, file)

# Generar y guardar los embeddings de cada documento PDF
documents_folder = 'documentos'
embeddings_folder = 'embeddings'

print(f"Listando documentos en: {documents_folder}")
for filename in os.listdir(documents_folder):
    if filename.endswith(".pdf"):
        print(f"Procesando archivo: {filename}")
        pdf_path = os.path.join(documents_folder, filename)
        embeddings = generate_embeddings(pdf_path)
        output_file = os.path.join(embeddings_folder, os.path.splitext(filename)[0] + '_embedding.json')
        save_embeddings(embeddings, output_file)

print("Proceso completado.")