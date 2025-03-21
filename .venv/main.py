import re
import pandas as pd
import PyPDF2

# Caminho do arquivo PDF
pdf_path = ".venv/lista.pdf"
# xml_output_path = ".venv/ranking_candidatos.xml"

# Função para extrair texto do PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            print(page.extract_text())
            break
            # text += page.extract_text() + "\n"
    # print("Texto extraído (primeiros 1000 caracteres):")
    # print(text[:1000])  # Mostra apenas os primeiros 1000 caracteres
    return text

# Extrair texto do PDF
pdf_text = extract_text_from_pdf(pdf_path)
